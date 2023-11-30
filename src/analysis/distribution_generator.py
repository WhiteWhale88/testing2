"""
 Генерация плотностей распределений

 (C) 2023 Alisa Haidarova, PetrGU, Petrozavodsk, Russia
 License: GNU General Public License (GPL)
 Email: i.nesy.chav@gmail.com
"""

import sympy as sp
import numpy as np

def norm(average: float, scale: float, edges: np.ndarray):
    """
    Вычисляет плотность для нормального распределения.

    Параметры
    ----------
    average: float
        среднее
    scale: float
        стандартное отклонение
    edges: np.ndarray
        числа, относительно которых вычисляется плотность

    Возвращает
    ----------
     : np.ndarray
        плотность нормального распределения
    """
    const = 1 / (scale * sp.sqrt(2 * np.pi))
    arr = np.array([const * sp.exp(-((x - average) ** 2) / (2 * scale**2)) for x in edges])
    return arr / arr.sum()


def expon(lambd: float, edges: np.ndarray):
    """
    Вычисляет плотность для экспоненциального распределения.

    Параметры
    ----------
    lambd: float
        интенсивность (обратный коэффициент масштаба)
    edges: np.ndarray
        числа, относительно которых вычисляется плотность

    Возвращает
    ----------
     : np.ndarray
        плотность экспоненциального распределения
    """
    arr = np.array([lambd * sp.exp(-lambd * x) for x in edges])
    return arr / arr.sum()


def gamma(alpha: float, beta: float, edges: np.ndarray):
    """
    Вычисляет плотность для гамма распределения.

    Параметры
    ----------
    alpha: float
        форма
    beta: float
        масштаб
    edges: np.ndarray
        числа, относительно которых вычисляется плотность

    Возвращает
    ----------
     : np.ndarray
        плотность гамма распределения
    """
    const = 1 / sp.gamma(alpha) * beta**alpha
    arr = np.array([const * x ** (alpha - 1) * sp.exp(-x / beta) for x in edges])
    return arr / arr.sum()
