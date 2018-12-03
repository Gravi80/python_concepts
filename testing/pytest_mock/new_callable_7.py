# Patch object by default creates MagicMock
# We can use some other object instead of MagicMock using 'new_callable' Or 'new'
from mock import patch


class Foo:
    x = 10


class Bar:
    x = 20


# replace Magic mock with a callable Object
def test_new_callable():
    with patch('new_callable_7.Foo', new_callable=Bar) as mock_foo:
        assert mock_foo.x == 20
        assert isinstance(mock_foo, Bar)


# 'new' will replace MagicMock with an object that already exists
def test_new():
    foo = 'Hello'
    with patch('new_callable_7.Foo', new=foo) as mock_foo:
        assert mock_foo == 'Hello'
