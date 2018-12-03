# MagicMock is a subclass of Mock with default implementations of most of the magic methods.
# implements default magic or dunder methods.
# https://docs.python.org/dev/library/unittest.mock.html#unittest.mock.MagicMock

from mock import MagicMock, Mock, NonCallableMock, NonCallableMagicMock


def test_magic_mock_dir():
    mock = Mock()
    magic_mock = MagicMock()
    assert dir(mock) == dir(magic_mock)
    int(magic_mock)
    assert dir(mock) != dir(magic_mock)


def test_magic_mock():
    magic_mock = MagicMock()
    mock = Mock()
    len(magic_mock)
    try:
        len(mock)
    except TypeError:
        print("'Mock' has no len()")


mocks = [
    Mock(),
    MagicMock(),
    NonCallableMock(),
    NonCallableMagicMock()
]
