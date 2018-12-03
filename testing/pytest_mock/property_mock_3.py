from mock import PropertyMock, patch, call, MagicMock


# PropertyMock provides __get__() and __set__() methods so you can specify a return value
# when it is fetched.

class Foo(object):
    @property
    def foo(self):
        return 'something'

    @foo.setter
    def foo(self, value):
        pass


def test_property_mock():
    with patch('property_mock_3.Foo.foo', new_callable=PropertyMock) as mock_foo:
        mock_foo.return_value = 'mockity-mock'
        this_foo = Foo()
        print(this_foo.foo)
        this_foo.foo = 6

        # Fetching a PropertyMock instance from an object calls the mock, with no args.
        # Setting it calls the mock with the value being set.
        assert mock_foo.mock_calls == [call(), call(6)]


def test_property_mock_dynamic_set():
    m = MagicMock()
    p = PropertyMock(return_value=3)
    type(m).foo = p

    assert m.foo == 3
    p.assert_called_once()
