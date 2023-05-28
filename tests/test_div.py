import pytest

from pracci import PracCiCalculator


@pytest.fixture(scope='function')
def calculator() -> PracCiCalculator:
    yield PracCiCalculator()


def test_success(calculator: PracCiCalculator):
    output = calculator.div(4, 2)
    answer = 4 / 2
    assert output == answer

def test_try_div_by_zero(calculator: PracCiCalculator):
    assert calculator.div(4, 0) is None
