from main import sol
import pytest

# @pytest.mark.skip('no')
@pytest.mark.parametrize('param,expected', [
    (2, 2),
    (3, 3),
    (5, 8)
])
def test_sol_70(param, expected):
    assert sol(param) == expected
