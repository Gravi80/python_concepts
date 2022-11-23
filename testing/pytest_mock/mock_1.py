# The main characteristic of a Mock object is that it will return another Mock instance when:
# accessing one of its attributes
# calling the object itself
from functools import partial

from mock import Mock, call


def test_should_test_mock():
    m = Mock()

    m.configure_mock(bar='baz')
    m.configure_mock(baz=lambda: 'baz')

    assert isinstance(m.foo, Mock)
    assert isinstance(m.foo(), Mock)
    assert isinstance(m(), Mock)

    assert m.foo is not m.foo() is not m()
    assert 'baz' == m.bar
    assert 'baz' == m.baz()


def test_return_value():
    m = Mock()
    m.return_value = 42
    assert m() == 42


def test_side_effect():
    m = Mock()
    m.side_effect = ['foo', 'bar', 'baz']
    assert m() == 'foo'
    assert m() == 'bar'
    assert m() == 'baz'


def _mock_some_url_response(actual_value, different_response_for_input):
    if actual_value == different_response_for_input:
        return "different result"
    else:
        return "same input"


def test_conditional_side_effect():
    mocked_function = Mock()
    different_response_for_input = 3
    mocked_function.side_effect = partial(_mock_some_url_response,
                                          different_response_for_input=different_response_for_input)
    assert mocked_function(1) == 'same input'
    assert mocked_function(2) == 'same input'
    assert mocked_function(3) == 'different result'


def test_raise_exception():
    m = Mock()
    m.side_effect = RuntimeError('Error')
    try:
        m()
    except RuntimeError:
        assert True
    else:
        assert False


# m.call_count to retrieve the number of calls to the Mock,
# m.call_args or m.call_args_list to inspect the arguments to the last or all calls respectively.
def test_call_count():
    m = Mock()

    m(1, 2)
    m(3, 4)

    assert 2 == m.call_count
    assert call(3, 4) == m.call_args
    assert [call(1, 2), call(3, 4)] == m.call_args_list


# m.reset_mock() method to clear the recorded interactions(configuration will not be reset).
def test_reset_mock():
    m = Mock()
    m.configure_mock(bar='baz')

    m(1, 2)
    m(3, 4)

    m.reset_mock()

    assert 0 == m.call_count
    assert None == m.call_args
    assert [] == m.call_args_list
    assert 'baz' == m.bar
