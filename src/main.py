"""
 Анализ данных файла

 (C) 2023 Alisa Haidarova, PetrGU, Petrozavodsk, Russia
 License: GNU General Public License (GPL)
 Email: i.nesy.chav@gmail.com
"""

import dearpygui.dearpygui as dpg
import numpy as np
from analysis import sample_characteristics as sc


def add_data_plot(name_distrib, x_data, str_data, gen_data):
    """
    Отрисовка полученной информации на график.
    """
    dpg.set_value("freg_1", [x_data, list(str_data)])
    dpg.set_value("freg_2", [x_data, list(gen_data)])
    dpg.set_item_label("freg_2", name_distrib)


def get_data_file(path_file):
    """
    Чтение данных из файла.
    """
    try:
        file_data = np.genfromtxt(path_file, delimiter="\t", dtype=str)
        file_data = np.array(
            [float(elem.replace(",", ".").replace('"', "")) for elem in file_data]
        )
    except FileNotFoundError:
        return np.array([]), "Файл не найден."
    except (ValueError, TypeError):
        return np.array([]), "Данные не могут быть преобразованы в числа."
    return file_data, "Успешно открыт и считан"


def analyze_data():
    """
    Анализ данных файла.
    """

    # Чтение файла и преобразование данных
    file_data, result = get_data_file(dpg.get_value("file"))
    dpg.set_value("open_result", result)
    if not np.any(file_data):
        return

    # Вычисление статистических характеристик
    dict_params = sc.calculate_statistics(file_data)
    for key, value in dict_params.items():
        dpg.set_value(key, value)

    # Определение количества интервалов
    count_inter = round(5 * np.log10(dict_params["max"] - dict_params["min"]))
    x_data = list(range(count_inter))
    dpg.set_value("count_range", count_inter)

    # Нахождение относительных частот исходных данных
    src_data, edges = sc.break_array(file_data, count_inter)

    # Нахождение относительных частот данных для сравнения
    norm, exp, gamma = sc.number_generation(
        dict_params["mean"], dict_params["variance"], edges
    )

    # Отображение графика
    name_distrib = ["Норм. распр. выборка",
                    "Экс. распр. выборка",
                    "Гамма распр. выборка"]
    value_distrib = [norm, exp, gamma]
    index = sc.compare_distrib(src_data, value_distrib)
    add_data_plot(name_distrib[index], x_data, src_data, value_distrib[index])


def main():
    """
    Реализация интерфейса.
    """
    dpg.create_context()

    # Настройка шрифта
    with dpg.font_registry():
        with dpg.font(r"..\fonts\caviar-dreams.ttf", 20) as font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

    # Окно программы
    with dpg.window(tag="Primary Window"):
        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("ФАЙЛ С ВЫБОРКОЙ")
                dpg.add_input_text(
                    default_value="D:/Python/testing2/data/numbers1.csv",
                    width=500,
                    tag="file",
                )
                dpg.add_button(label="Анализировать", callback=analyze_data)
                dpg.add_text("Сообщение о чтении файла: ")
                dpg.add_text("", tag="open_result")
                dpg.add_text("ПАРАМЕТРЫ ВЫБОРКИ")
                dpg.add_input_text(
                    label="Количество элементов", width=200, tag="count", readonly=True
                )
                dpg.add_input_text(
                    label="Сумма элементов", width=200, tag="sum", readonly=True
                )
                dpg.add_input_text(
                    label="Количество диапазонов",
                    width=200,
                    tag="count_range",
                    readonly=True,
                )
                dpg.add_input_text(
                    label="Среднее выборочное", width=200, tag="mean", readonly=True
                )
                dpg.add_input_text(
                    label="Медиана", width=200, tag="median", readonly=True
                )
                dpg.add_input_text(
                    label="Дисперсия", width=200, tag="variance", readonly=True
                )
                dpg.add_input_text(
                    label="Среднеквадратичное отклонение",
                    width=200,
                    tag="scale",
                    readonly=True,
                )
                dpg.add_input_text(label="Минимум", width=200, tag="min", readonly=True)
                dpg.add_input_text(
                    label="Максимум", width=200, tag="max", readonly=True
                )
            with dpg.plot(
                label="Сравнение",
                width=700,
                height=500,
                tag="plot",
            ):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis")
                dpg.add_line_series(
                    [],
                    [],
                    label="Исходная выборка",
                    tag="freg_1",
                    parent="y_axis",
                )
                dpg.add_line_series(
                    [],
                    [],
                    label="",
                    tag="freg_2",
                    parent="y_axis",
                )
        dpg.bind_font(font)

    dpg.create_viewport(title="Generator", width=1200, height=700)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
