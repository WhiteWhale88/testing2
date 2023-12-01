"""
Тестирование модуля main
"""

import pytest
import numpy as np
from src import main


def test_analysis_data():
    """тест функции analysis_data"""
    src_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1, 2, 3])
    result = main.analysis_data(src_data)
    # проверка статистики
    assert result[0] == {
        "count": 15,
        "sum": 64,
        "mean": 4.266666666666667,
        "median": 3.0,
        "min": 1,
        "max": 10,
        "variance": 8.72888888888889,
        "scale": 2.9544693074880453,
    }
    # проверка количетсва разбиений
    assert result[1] == 5
    # проверка получившихся относительных частот
    true_freq = np.array([0.4, 0.2, 0.13333333, 0.13333333, 0.13333333])
    assert (result[2].all() == true_freq.all())
    # проверка подходящего распределения
    assert result[3] == "Экс. распр. выборка"
    # проверка значений подходящего распределения
    true_distrib = np.array([0.391702947613284,
                             0.256885064707034,
                             0.168469338491389,
                             0.110484889590971,
                             0.0724577595973228])
    assert result[4][0] == pytest.approx(true_distrib[0], abs=1e-6)
    assert result[4][1] == pytest.approx(true_distrib[1], abs=1e-6)
    assert result[4][2] == pytest.approx(true_distrib[2], abs=1e-6)
    assert result[4][3] == pytest.approx(true_distrib[3], abs=1e-6)
    assert result[4][4] == pytest.approx(true_distrib[4], abs=1e-6)


def test_get_data_file_not_found():
    """тест функции get_data_file - неверный путь к файлу"""
    file_data, result = main.get_data_file("numbers1.csv")

    assert not np.any(file_data)
    assert result == "Файл не найден."


def test_get_data_file_invalid_data(file_invalid_data):
    """тест функции get_data_file - нечитаемые данные"""
    file_data, result = main.get_data_file(file_invalid_data)

    assert not np.any(file_data)
    assert result == "Данные не могут быть преобразованы в числа."


def test_get_data_file_valid_data(file_valid_data):
    """тест функции get_data_file - верный путь к файлу и данные"""
    file_data, result = main.get_data_file(file_valid_data)

    assert file_data.all() == np.array([234.0, 67.99]).all()
    assert result == "Успешно открыт и считан"
