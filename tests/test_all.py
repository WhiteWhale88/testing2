"""
Тестирование
"""

import pytest
import sympy as sp
import numpy as np
from src.analysis import sample_characteristics as sc
from src.analysis import distribution_generator as dg
from src import main

class TestMain:
    """
    Тестирование модуля main
    """

    def test_get_data_file_not_found(self):
        """тест функции get_data_file - неверный путь к файлу"""
        file_data, result = main.get_data_file("numbers1.csv")

        assert not np.any(file_data)
        assert result == "Файл не найден."


    def test_get_data_file_invalid_data(self, file_invalid_data):
        """тест функции get_data_file - нечитаемые данные"""
        file_data, result = main.get_data_file(file_invalid_data)

        assert not np.any(file_data)
        assert result == "Данные не могут быть преобразованы в числа."


    def test_get_data_file_valid_data(self, file_valid_data):
        """тест функции get_data_file - верный путь к файлу и данные"""
        file_data, result = main.get_data_file(file_valid_data)

        assert file_data.all() == np.array([234.0, 67.99]).all()
        assert result == "Успешно открыт и считан"


class TestSampleCharacteristics:
    """
    Тестирование модуля sample_characteristics
    """

    def test_calculate_statistics(self):
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
            "standard_deviation": 1.4142135623730951,
        }

        assert sc.calculate_statistics(arr) == true_dict


    def test_break_array(self):
        """тест функции break_array"""
        arr = np.array([1,2,2,2,3,4,5,6])
        count_inter = 2

        true_freq = np.array([0.625, 0.375])
        true_edges = np.array([3., 6.])

        result_freq, result_edges = sc.break_array(arr, count_inter)

        assert result_freq.all() == true_freq.all()
        assert result_edges.all() == true_edges.all()


    def test_number_generation(self):
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


    def test_compare_distrib(self):
        """тест функции compare_distrib"""
        src = np.array([1, 2, 3])
        arr_distrib = np.array([[0.5, 2.3, 1.5], [0, -5., 9.]])
        assert sc.compare_distrib(src, arr_distrib) == 0


class TestDistributionGenerator:
    """
    Тестирование модуля distribution_generator
    """

    def test_norm(self):
        """тест функции norm"""
        average = 5.
        scale = sp.sqrt(3)
        edges = [3., 6.]
        result = dg.norm(average, scale, edges)
        assert result[0] == pytest.approx(0.377540668798145, abs=1e-6)
        assert result[1] == pytest.approx(0.622459331201855, abs=1e-6)


    def test_expon(self):
        """тест функции expon"""
        lambd = 1. / 5.
        edges = [3., 6.]
        result = dg.expon(lambd, edges)
        assert result[0] == pytest.approx(0.645656306225796, abs=1e-6)
        assert result[1] == pytest.approx(0.354343693774204, abs=1e-6)
        

    def test_gamma(self):
        """тест функции gamma"""
        alpha = 8.33333333333333
        beta = 0.6
        edges = [3., 6.]
        result = dg.gamma(alpha, beta, edges)
        assert result[0] == pytest.approx(0.479242107149368, abs=1e-6)
        assert result[1] == pytest.approx(0.520757892850632, abs=1e-6)
