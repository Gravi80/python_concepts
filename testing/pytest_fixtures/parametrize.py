# pytest testing/pytest_fixtures/parametrize.py -v -s
# Parametrize tests
import pytest


@pytest.fixture(params=['apple', 'banana', 'plum'])
def fruit(request):
    print(f"####{request.function.__name__}######")
    print(f"####{request.cls}######")
    return request.param


def test_is_healthy(fruit):
    assert (fruit in ['apple', 'banana', 'plum']) is True
