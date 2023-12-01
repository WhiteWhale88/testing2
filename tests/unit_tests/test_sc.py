"""
Тестирование модуля sample_characteristics
"""

import pytest
import numpy as np
from src.analysis import sample_characteristics as sc

def test_calculate_statistics():
    """тест функции calculate_statistics"""
    arr = np.array([1, 2, 3, 4, 5])
    true_dict = {
        "count": 5,
        "sum": 15,
        "mean": 3.0,
        "median": 3.0,
        "min": 1,
        "max": 5,
        "variance": 2.0,
        "scale": 1.4142135623730951,
    }

    assert sc.calculate_statistics(arr) == true_dict


def test_break_array():
    """тест функции break_array"""
    arr = np.array([1,2,2,2,3,4,5,6])
    count_inter = 2

    true_freq = np.array([0.625, 0.375])
    true_edges = np.array([3., 6.])

    result_freq, result_edges = sc.break_array(arr, count_inter)

    assert result_freq.all() == true_freq.all()
    assert result_edges.all() == true_edges.all()


def test_number_generation():
    """тест функции number_generation"""
    average = 5.
    var = 3.
    edges = [3., 6.]
    true_norm = np.array([0.377540668798145, 0.622459331201855])
    true_exp = np.array([0.645656306225796, 0.354343693774204])
    true_gamma = np.array([0.479242107149368, 0.520757892850632])

    result_norm, result_exp, result_gamma = sc.number_generation(average, var, edges)

    assert result_norm[0] == pytest.approx(true_norm[0], abs=1e-6)
    assert result_norm[1] == pytest.approx(true_norm[1], abs=1e-6)

    assert result_exp[0] == pytest.approx(true_exp[0], abs=1e-6)
    assert result_exp[1] == pytest.approx(true_exp[1], abs=1e-6)

    assert result_gamma[0] == pytest.approx(true_gamma[0], abs=1e-6)
    assert result_gamma[1] == pytest.approx(true_gamma[1], abs=1e-6)


def test_compare_distrib():
    """тест функции compare_distrib"""
    src = np.array([1, 2, 3])
    arr_distrib = np.array([[0.5, 2.3, 1.5], [0, -5., 9.]])
    assert sc.compare_distrib(src, arr_distrib) == 0
