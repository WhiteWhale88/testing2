"""
Тестирование модулей sample_characteristics и distribution_generator
"""

import pytest
import numpy as np
from src.analysis import sample_characteristics as sc
from src.analysis import distribution_generator as dg

def test_calculate_statistics_norm():
    """тест функций calculate_statistics и norm"""
    arr = np.array([1, 2, 3, 4, 5])
    count_inter = 2
    stats = sc.calculate_statistics(arr)
    _, edges = sc.break_array(arr, count_inter)
    result = dg.norm(stats["mean"], np.sqrt(stats["variance"]), edges)
    assert result[0] == pytest.approx(0.731058578630005, abs=1e-6)
    assert result[1] == pytest.approx(0.268941421369995, abs=1e-6)


def test_number_generation_norm():
    """тест функций number_generation и norm"""
    average = 3.
    var = 2.
    edges = [3., 5.]
    arr_cs, _, _ = sc.number_generation(average, var, edges)
    arr_dg = dg.norm(average, np.sqrt(var), edges)
    assert arr_cs.all() == arr_dg.all()


def test_number_generation_expon():
    """тест функций number_generation и expon"""
    average = 3.
    var = 2.
    lambd = 1 / average
    edges = [3., 5.]
    _, arr_cs, _ = sc.number_generation(average, var, edges)
    arr_dg = dg.expon(lambd, edges)
    assert arr_cs.all() == arr_dg.all()


def test_number_generation_gamma():
    """тест функций number_generation и gamma"""
    alpha = 3.
    beta = 0.5
    average = alpha * beta
    var = alpha * beta**2
    edges = [3., 5.]
    _, _, arr_cs = sc.number_generation(average, var, edges)
    arr_dg = dg.gamma(alpha, beta, edges)
    assert arr_cs.all() == arr_dg.all()
