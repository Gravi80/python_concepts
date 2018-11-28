# pytest testing/pytest_fixtures/use_fixtures.py -v -s
import pytest


# Sometimes test functions do not directly need access to a fixture object. The fixture can be in
# conftest.py

@pytest.fixture()
def fix1():
    print("*******Fix 1 called*******")
    return "Fix1"


@pytest.fixture()
def fix2():
    print("*******Fix 2 called*******")
    return "Fix2"


@pytest.mark.usefixtures("fix1", "fix2")
def test_1(fix1, fix2):
    assert "Fix1" == fix1
    assert "Fix2" == fix2
