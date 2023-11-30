"""
Тестирование
"""


import numpy as np
from src.analytic import analysis
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


class TestAnalysis:
    """
    Тестирование модуля analysis
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
        assert analysis.calculate_statistics(arr) == true_dict

    def test_get_partition(self):
        """тест функции get_partition"""
        arr = np.array([1, 2, 2, 2, 3, 4, 5, 6])
        count_inter = 2
        true_result = np.array([[0, 1], np.array([0.625, 0.375])])
        assert analysis.get_partition(arr, count_inter).all() == true_result.all()

    def test_number_generation(self):
        """тест функции number_generation"""
        average = 5.0
        var = 3.0
        size = 100
        count_inter = 5
        true_norm = np.array(
            [
                [0, 1, 2, 3, 4],
                np.array([0.04, 0.21, 0.47, 0.24, 0.04]),
            ]
        )
        true_exp = np.array(
            [
                [0, 1, 2, 3, 4],
                np.array([0.77, 0.13, 0.07, 0.02, 0.01]),
            ]
        )
        true_gamma = np.array(
            [
                [0, 1, 2, 3, 4],
                np.array([0.17, 0.46, 0.27, 0.07, 0.03]),
            ]
        )

        np.random.seed(12)
        norm, exp, gamma = analysis.number_generation(average, var, size, count_inter)

        assert norm.all() == true_norm.all()
        assert exp.all() == true_exp.all()
        assert gamma.all() == true_gamma.all()

    def test_compare_distrib(self):
        """тест функции compare_distrib"""
        arr = np.array([1, 2, 3])
        lst = [np.array([0.5, 2.3, 1.5]), np.array([0, -5, 9])]
        assert analysis.compare_distrib(arr, lst) == 0
