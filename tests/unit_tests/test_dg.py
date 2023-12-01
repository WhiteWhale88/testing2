"""
Тестирование модуля distribution_generator
"""

import pytest
import sympy as sp
from src.analysis import distribution_generator as dg


def test_norm():
    """тест функции norm"""
    average = 5.
    scale = sp.sqrt(3)
    edges = [3., 6.]
    result = dg.norm(average, scale, edges)
    assert result[0] == pytest.approx(0.377540668798145, abs=1e-6)
    assert result[1] == pytest.approx(0.622459331201855, abs=1e-6)


def test_expon():
    """тест функции expon"""
    lambd = 1. / 5.
    edges = [3., 6.]
    result = dg.expon(lambd, edges)
    assert result[0] == pytest.approx(0.645656306225796, abs=1e-6)
    assert result[1] == pytest.approx(0.354343693774204, abs=1e-6)


def test_gamma():
    """тест функции gamma"""
    alpha = 8.33333333333333
    beta =0.6
    edges = [3., 6.]
    result = dg.gamma(alpha, beta, edges)
    assert result[0] == pytest.approx(0.479242107149368, abs=1e-6)
    assert result[1] == pytest.approx(0.520757892850632, abs=1e-6)
