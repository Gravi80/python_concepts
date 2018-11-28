# pytest testing/pytest_fixtures/scope_order.py -v -s
import pytest


class TestClass:

    @pytest.fixture(scope='session')
    def once_for_pytest_session(self):
        print("*********once_for_pytest_session*********")

    @pytest.fixture(scope='package')
    def once_for_package(self, once_for_pytest_session):
        print("*********once_for_package*********")

    @pytest.fixture(scope='module')
    def once_for_module(self, once_for_package):
        print("*********once_for_module*********")

    @pytest.fixture(scope='class')
    def once_for_class(self, once_for_module):
        print("*********once_for_class*********")

    @pytest.fixture(scope='function')
    def each_function(self, once_for_class):
        print("*********each_function*********")

    def test_scope_order(self, each_function):
        pass

    def test_scope_order2(self, each_function, once_for_class, once_for_pytest_session):
        pass
