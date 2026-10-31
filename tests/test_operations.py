import pytest

from app.operations import somar


@pytest.mark.parametrize(("a", "b", "esperado"), [(2, 3, 5), (-1, 1, 0), (0.1, 0.2, 0.3)]) 
def test_somar(a, b, esperado): 
    assert somar(a, b) == pytest.approx(esperado)
    