'''
Тестирование
'''

import pytest
import numpy as np
from src.analytic import analysis


class TestAnalysis():
    '''
    Тестирование модуля analysis
    '''

    @pytest.mark.calculate_statistics
    def test_calculate_statistics(self):
        ''' тест функции calculate_statistics'''
        arr = np.array([1,2,3,4,5])
        true_dict = {
            "count": 5,
            "sum": 15,
            "mean": 3.0,
            "median": 3.0,
            "min": 1,
            "max": 5,
            "variance": 2.0,
            "standard_deviation": 1.4142135623730951
        }
        assert analysis.calculate_statistics(arr) == true_dict


    @pytest.mark.get_partition
    def test_get_partition(self):
        ''' тест функции get_partition'''
        arr = np.array([1,2,2,2,3,4,5,6])
        count_inter = 2
        assert analysis.get_partition(arr, count_inter) == [[0, 1], [0.625, 0.375]]


    @pytest.mark.number_generation
    def test_number_generation(self):
        ''' тест функции number_generation'''
        average = 5.0
        var = 3.0
        size = 10
        true_norm = np.array([5.81923549, 3.81973576, 5.41991753, 2.05423947, 6.30448165,
                              2.34178466, 5.00888036, 4.79175957, 3.60226639, 9.9741371 ])
        true_exp = np.array([7.30798162, 0.87603514, 7.23150544, 0.10514687, 0.72634391,
                             0.61803554, 1.85457632, 5.56537148, 3.18600652, 8.46867302])
        true_gamma = np.array([6.7314887 , 3.41014754, 5.70307387, 5.03950646, 3.09540968,
                               2.4742548 , 2.36004233, 3.9579512 , 4.73376682, 4.38187534])
        norm, exp, gamma = analysis.number_generation(average, var, size)
        assert norm.all() == true_norm.all()
        assert exp.all() == true_exp.all()
        assert gamma.all() == true_gamma.all()

#if __name__ == "__main__":
#    main()
