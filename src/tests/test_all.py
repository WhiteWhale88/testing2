from unittest import TestCase, main
import numpy as np
from src.analitic import analysis


class TestAnalysis(TestCase):
    def test_calculate_statistics(self):
        arr = np.array([1,2,3,4,5])
        true_dict = {
            "count": 5,
            "sum": 15,
            "mean": 3.0,
            "median": 3.0,
            "min": 1,
            "max": 2,
            "variance": 2.0,
            "standard_deviation": 1.4142135623730951
        }
        self.assertEqual(analysis.calculate_statistics(arr), true_dict)


    def test_get_partition(self):
        arr = np.array([1,2,2,2,3,4,5,6])
        count_inter = 2
        self.assertEqual(analysis.get_partition(arr, count_inter), [[0, 1], [0.625, 0.375]])


    def test_number_generation(self):
        average = 5.0
        var = 3.0
        size = 10
        self.assertEqual(analysis.number_generation(average, var, size),
                         (np.array([5.81923549, 3.81973576, 5.41991753, 2.05423947, 6.30448165,
                                    2.34178466, 5.00888036, 4.79175957, 3.60226639, 9.9741371 ]),
                          np.array([7.30798162, 0.87603514, 7.23150544, 0.10514687, 0.72634391,
                                    0.61803554, 1.85457632, 5.56537148, 3.18600652, 8.46867302]),
                          np.array([6.7314887 , 3.41014754, 5.70307387, 5.03950646, 3.09540968,
                                    2.4742548 , 2.36004233, 3.9579512 , 4.73376682, 4.38187534])))


if __name__ == "__main__":
    main()




