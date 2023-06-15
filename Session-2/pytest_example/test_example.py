from example import add, subtract, divide
import pytest

num1 = 50
num2 = 5


@pytest.fixture
def prep_fancy_data():
    fancy_data = 5 * 5 + 5 / 5
    return fancy_data


def test_fancy_foo(prep_fancy_data):
    assert prep_fancy_data == 26


@pytest.mark.g1
def test_add():
    output = add(num1, num2)
    assert output == 55


@pytest.mark.g1
def test_subtract():
    output = subtract(num1, num2)
    assert output == 45


@pytest.mark.g1
def test_divide():
    output = divide(num1, num2)
    assert output == 10
