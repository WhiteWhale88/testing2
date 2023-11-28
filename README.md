| general information | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=WhiteWhale88_testing2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=WhiteWhale88_testing2) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=WhiteWhale88_testing2&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=WhiteWhale88_testing2) |
| сode                | [![Pylint](https://github.com/WhiteWhale88/testing2/actions/workflows/pylint.yml/badge.svg)](https://github.com/WhiteWhale88/testing2/actions/workflows/pylint.yml) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=WhiteWhale88_testing2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=WhiteWhale88_testing2) |
| tests               | [![Automated tests](https://github.com/WhiteWhale88/testing2/actions/workflows/test-action.yml/badge.svg)](https://github.com/WhiteWhale88/testing2/actions/workflows/test-action.yml) [![Python application](https://github.com/WhiteWhale88/testing2/actions/workflows/python-app.yml/badge.svg)](https://github.com/WhiteWhale88/testing2/actions/workflows/python-app.yml) |
| сoverage            | [![Coverage Status](https://coveralls.io/repos/github/WhiteWhale88/testing2/badge.svg?branch=main)](https://coveralls.io/github/WhiteWhale88/testing2?branch=main) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=WhiteWhale88_testing2&metric=coverage)](https://sonarcloud.io/summary/new_code?id=WhiteWhale88_testing2) |


# Описание программы

Программа считывает файл csv с данными, преобразует их и сравнивает с существующими тремя распределениями: нормальное, экспоненциальное и гамма.

# План тестирования

## Аттестационные тесты

* Тест А1 (позитивный)
+ Начальное состояние: Запущена программа
+ Действие: Ввод названия файла: "D:/Python/testing2/data/numbers1.csv", нажатие на кнопку "Analyze"
+ Ожидаемы результат:
    ```
	Вывод сообщения: "Успешно открыт и считан"
    Вывод всех параметров выборки и отрисовка графиков
    ```

* Тест А2 (негативный)
+ Начальное состояние: Открытый терминал
+ Действие: Ввод названия файла: "D:/Python/testing2/data/numbers11.csv", нажатие на кнопку "Analyze"
+ Ожидаемы результат:
    ```
    Вывод сообщения: "D:/Python/testing2/data/numbers11.csv not found"
    ```

## Блочное тестирование

### Модуль analysis.py

* Тест Б1.1 (позитивный)
+ Функция: calculate_statistics(arr : np.array)
+ Входные данные: np.array([1,2,3,4,5])
+ Ожидаемый результат:
	```
	{
        "count": 5,
        "sum": 15,
        "mean": 3.0,
        "median": 3.0,
        "min": 1,
        "max": 2,
        "variance": 2.0,
        "standard_deviation": 1.4142135623730951
    }
	```

* Тест Б1.2 (позитивный)
+ Функция: get_partition(arr: np.ndarray, count_inter: int)
+ Входные данные: np.array([1,2,2,2,3,4,5,6]), 2
+ Ожидаемы результат:
	```
	[[0, 1], [0.625, 0.375]]
	```

* Тест Б1.3 (позитивный)
+ Функция: number_generation(average: float, var: float, size: int)
+ Входные данные: 5.0, 3.0, 10
+ Ожидаемы результат:
	```
	(array([5.81923549, 3.81973576, 5.41991753, 2.05423947, 6.30448165,
       2.34178466, 5.00888036, 4.79175957, 3.60226639, 9.9741371 ]),
	array([7.30798162, 0.87603514, 7.23150544, 0.10514687, 0.72634391,
       0.61803554, 1.85457632, 5.56537148, 3.18600652, 8.46867302]),
	array([6.7314887 , 3.41014754, 5.70307387, 5.03950646, 3.09540968,
       2.4742548 , 2.36004233, 3.9579512 , 4.73376682, 4.38187534]))
	```

## Интеграционное тестирование

* Тест И1 (позитивный)