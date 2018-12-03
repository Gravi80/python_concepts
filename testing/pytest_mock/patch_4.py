import os
from io import StringIO

from mock import mock, patch, DEFAULT, MagicMock


def pwd():
    path = os.getcwd()
    print(f'Working on {path}')
    return path


@mock.patch('patch_4.os')
def test_func_patch(mocked_os):
    pwd()
    mocked_os.getcwd.assert_called_once()


@mock.patch('patch_4.os.getcwd', return_value='testing')
def test_patch_return_value(mocked_getcwd):
    current_dir = pwd()
    mocked_getcwd.assert_called_once()
    assert current_dir == 'testing'


# Use context managers to patch built-ins
def test_patch_built_ins():
    with patch('os.curdir') as curdir_mock:  # curdir_mock lives only inside with block. Doesn't lives outside
        assert curdir_mock == os.curdir
    assert os.curdir == '.'


class Class1:

    def __init__(self, name):
        self.name = name

    def method1(self):
        return "class1 method1"


class Class2:
    def __init__(self):
        self.class1 = Class1('class1')

    def method2(self):
        result = self.class1.method1()
        print(f'Result= {result}')
        return result

    def method3(self):
        return 'method3'


def test_patch_class_completely():
    with mock.patch('patch_4.Class1') as MockClass1:
        MockClass1.return_value.method1.return_value = 'testing'
        class2 = Class2()
        MockClass1.assert_called_once_with('class1')
        assert class2.method2() == 'testing'


# only respond to methods that actually exist in the spec class.  [#NonCallableMagicMock]
class Foo:
    x = 10

    def bar(self, x):
        y = 20 + x
        return y


def test_spec_false():
    with mock.patch('patch_4.Foo') as mock_foo:  # mock_foo is a MagicMock object but has no
        # knowledge about object it's patching.
        assert ('x' in dir(mock_foo)) is False
        assert ('bar' in dir(mock_foo)) is False


def test_spec_true():
    with mock.patch('patch_4.Foo', spec=True) as mock_foo:  # mock_foo is a MagicMock object that looks
        # like the object that it is patching.
        assert ('x' in dir(mock_foo)) is True
        assert ('bar' in dir(mock_foo)) is True
        try:
            mock_foo.random_method.return_value = 'testing'
        except AttributeError:
            print("Mock object has no attribute 'missing_method'")


# spec, autospec : Prevents from accessing attributes that don't exists
# specset : Prevents from setting attributes that don't exists
# spec doesn't know about the attributes -> attributes
def test_spec():
    with mock.patch('patch_4.Foo', spec=True) as mock_foo:
        foo = Foo()
        foo.bar()  # Tests passes even if the foo attribute is called with invalid attributes
        mock_foo.return_value.bar.assert_called_once_with()


# autospec: Stricter form of spec
# Will find attributes -> attributes
def test_autospec():
    with mock.patch('patch_4.Foo', autospec=True) as mock_foo:
        foo = Foo()
        try:
            foo.bar()
        except TypeError:
            print('TypeError: missing a required argument: x')


# autospec doesn't know about dynamically created attributes (Ex-any attribute within __init__)
class FooBar:
    def __init__(self):
        x = 20

    def bar(self):
        pass


def test_autospec_issue():
    with mock.patch('patch_4.FooBar', autospec=True) as mock_foobar:
        foobar = mock_foobar()
        foobar.bar
        try:
            foobar.x
        except AttributeError:
            print('AttributeError: Mock object has no attribute x')


def test_autospec_issue_fix1():
    with mock.patch('patch_4.FooBar', autospec=True) as mock_foobar:
        foobar = mock_foobar()
        foobar.bar
        foobar.x = 20  # But might be a problem where people can set any attribute on Mock
        foobar.x


# spec_set: prevents you setting any attribute that don't exists
def test_spec_set():
    with mock.patch('patch_4.FooBar', autospec=True, spec_set=True) as mock_foobar:
        foobar = mock_foobar()
        foobar.bar
        try:
            foobar.x = 20
        except AttributeError:
            print('AttributeError: Mock object has no attribute x')


@patch.object(FooBar, 'x', create=True)  # Create an attribute if it doesn't exists
def test_autospec_issue_fix2(mock_x):
    with mock.patch('patch_4.FooBar', autospec=True, spec_set=True) as mock_foobar:
        foobar = mock_foobar()
        foobar.x = 10


# Partial mocking
def test_partial_patching():
    with mock.patch.object(Class1, 'method1', return_value='testing') as method1_mock:
        class2 = Class2()
        assert class2.method2() == 'testing'
        method1_mock.assert_called_once()


# Patch a dictionary, or dictionary like object, and
# restore the dictionary to its original state after the test.
@mock.patch.dict('patch_4.os.environ', {'MY_VAR': 'testing'})
def test_patch_builtin_dict_decorators():
    assert os.environ.get('MY_VAR') == 'testing'


# context managers
def size_of():
    with open('text.txt') as f:
        contents = f.read()

    return len(contents)


def test_context_manager():
    with mock.patch('patch_4.open') as mock_open:
        mock_open.return_value.__enter__.return_value = StringIO('testing')
        assert size_of() == 7


# Patch multiple objects
# Use DEFAULT as the value if you want patch.multiple() to create mocks for you.
# All arguments MUST be attribute of the same object.

# Can patch all the import Classes
@patch.multiple('patch_4', Class1=DEFAULT, Class2=DEFAULT)
def test_function(**mocks):
    assert isinstance(mocks['Class1'], MagicMock)
    assert isinstance(mocks['Class2'], MagicMock)
