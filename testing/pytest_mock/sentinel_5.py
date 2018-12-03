# create_autospec
# unittest.mock.ANY
# mock_open
from mock import Mock, sentinel, patch, ANY


# Sometimes when testing you need to test that a specific object is passed as an argument
# to another method, or returned.
def test_sentinel():
    class1 = Mock("Class1")
    class1.method = Mock(name="method")
    class1.method.return_value = sentinel.some_object
    result = class1.method()
    assert result is sentinel.some_object


def sum(a, b):
    return a + b


@patch('sentinel_5.sum')
def test_any(sum_mock):
    sum(1, 2)

    sum_mock.assert_called_once_with(1, ANY)
