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
def test_autospec():
    with mock.patch('patch_4.Class1', autospec=True) as MockClass1:
        MockClass1.return_value.method1.return_value = 'testing'
        class2 = Class2()
        MockClass1.assert_called_once_with('class1')
        assert class2.method2() == 'testing'
        try:
            MockClass1.return_value.missing_method.return_value = 'testing'
        except AttributeError:
            print("Mock object has no attribute 'missing_method'")


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
