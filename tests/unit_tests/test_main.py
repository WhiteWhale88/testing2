"""
Тестирование модуля main
"""

import pytest
import numpy as np
from src import main


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
