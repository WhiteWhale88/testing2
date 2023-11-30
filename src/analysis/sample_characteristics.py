"""
 Анализ набора данных

 (C) 2023 Alisa Haidarova, PetrGU, Petrozavodsk, Russia
 License: GNU General Public License (GPL)
 Email: i.nesy.chav@gmail.com
"""

import sympy as sp
import numpy as np
import distribution_generator as dg

def calculate_statistics(arr: np.ndarray):
    """
    Возвращает статистические показатели для данных
    (размер, сумма, среднее, медиана, минимум, максимум,
    дисперсия, стандартное отклонение).

    Параметры
    ----------
    arr : np.ndarray
        одномерный массив элементов числового типа

    Возвращает
    ----------
    statistics_dict : dictinary
        словарь со статистическими показателями
    """
    statistics_dict = {
        "count": arr.size,
        "sum": arr.sum(),
        "mean": np.mean(arr),
        "median": np.median(arr),
        "min": arr.min(),
        "max": arr.max(),
        "variance": arr.var(),
        "standard_deviation": arr.std(),
    }
    return statistics_dict


def break_array(arr: np.ndarray, count_inter: int):
    """
    Определяет относительную частоту выборки

    Параметры
    ----------
    arr : np.ndarray
        одномерный массив элементов числового типа
    count_inter : int
        количество интервалов для разбиения

    Возвращает
    ----------
     : np.ndarray
        массив частот
    bin_edges[1:] : np.ndarray
        масссив верхних границ частот
    """
    hist, bin_edges = np.histogram(arr, count_inter)
    return hist / arr.size, bin_edges[1:]


def number_generation(average: float, var: float, edges: np.ndarray):
    """
    Генерирует распределения для определения исходной выборки

    Параметры
    ----------
    average : float
        среднее выборочной исходной выборки
    var : float
        дисперсия исходной выборки
    edges: np.ndarray
        границы разбиения исходной выборки

    Возвращает
    ----------
    norm_numbers : np.ndarray
        массив нормально распределенных значений
    exp_numbers : np.ndarray
        массив экспоненциально распределенных значений
    gamma_numbers : np.ndarray
        массив гамма распределенных значений
    """
    norm_numbers = dg.norm(average, np.sqrt(var), edges)

    exp_numbers = dg.expon(1 / average, edges)

    x, y = sp.symbols("x y")
    params = sp.solve([x * y - average, x * y**2 - var], [x, y])[0]
    gamma_numbers = dg.gamma(params[0], params[1], edges)

    return norm_numbers, exp_numbers, gamma_numbers


def compare_distrib(src: np.ndarray, arr_distrib: list):
    """
    Сравнивает значения исходной выборки со значениями
    предполагаемых распределений

    Параметры
    ----------
    src : np.ndarray
        исходная выборка
    arr_distrib : list
        список предполагаемых распределений

    Возвращает
    ----------
    index : int
        индекс самого похожего распределения
    """

    amount_of_difference = np.array([])
    for distrib in arr_distrib:
        amount_of_difference = np.append(
            amount_of_difference, np.sum(np.abs(src - distrib))
        )

    index = np.where(amount_of_difference == min(amount_of_difference))[0][0]
    return index
