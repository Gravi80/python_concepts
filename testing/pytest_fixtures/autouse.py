# pytest testing/pytest_fixtures/autouse.py -v -s
# Autouse fixtures
# fixtures get invoked automatically.
import pytest


@pytest.fixture(autouse=True)
def auto_trigger():
    print("*********** called auto_trigger ***********")


def test_should_run_auto_trigger():
    pass
