import pytest
from mock import patch


def name():
    return "Ravi"


def birthday():
    return "January"


def address():
    return "Delhi"


@patch('patch_start_stop_6.name', return_value='Name')
@patch('patch_start_stop_6.birthday', return_value='Birthday')
@patch('patch_start_stop_6.address', return_value='Address')
class Test1:

    def test_name_1(self, mock_address, mock_birthday, mock_name):
        assert address() == 'Address'
        assert birthday() == 'Birthday'
        assert name() == 'Name'

    def test_name_2(self, mock_address, mock_birthday, mock_name):
        assert address() == 'Address'
        assert birthday() == 'Birthday'
        assert name() == 'Name'


class Test2:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mock_name = patch('patch_start_stop_6.name').start()
        self.mock_birthday = patch('patch_start_stop_6.birthday').start()
        self.mock_address = patch('patch_start_stop_6.address').start()
        yield
        patch.stopall

    def test_name_1(self):
        self.mock_name.return_value = 'Test1Name'
        self.mock_birthday.return_value = 'Test1BirthDay'
        self.mock_address.return_value = 'Test1Address'
        assert address() == 'Test1Address'
        assert birthday() == 'Test1BirthDay'
        assert name() == 'Test1Name'

    def test_name_2(self):
        self.mock_name.return_value = 'Test2Name'
        self.mock_birthday.return_value = 'Test2BirthDay'
        self.mock_address.return_value = 'Test2Address'
        assert address() == 'Test2Address'
        assert birthday() == 'Test2BirthDay'
        assert name() == 'Test2Name'
