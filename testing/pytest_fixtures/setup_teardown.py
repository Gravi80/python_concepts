# pytest testing/pytest_fixtures/setup_teardown.py -v -s
# Setup and Teardown
# https://github.com/pytest-dev/pytest/blob/master/src/_pytest/fixtures.py#L820 (call_fixture_func)
# https://github.com/pytest-dev/pytest/blob/master/src/_pytest/fixtures.py#L969
# https://github.com/pytest-dev/pytest/blob/master/src/_pytest/fixtures.py#L825
# https://github.com/pytest-dev/pytest/blob/master/src/_pytest/fixtures.py#L832 (_teardown_yield_fixture)
import pytest


@pytest.fixture()
def browser():
    print("\n************Browser opened")
    yield "browser object"
    print("\n************browser closed")  # (The cleanup after the yield statement is run as a finalizer).


def test_should_run_setup_and_teardown(browser):
    print(f"\n************{browser}")
