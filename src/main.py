"""
 Анализ данных файла

 (C) 2023 Alisa Haidarova, PetrGU, Petrozavodsk, Russia
 License: GNU General Public License (GPL)
 Email: i.nesy.chav@gmail.com
"""

# pragma: cover

import dearpygui.dearpygui as dpg
import numpy as np
from analytic import analysis


def add_data_plot(name_gen, str_data, gen_data):
    """
    Отрисовка полученной информации на графиках.
    """
    dpg.set_value(f"freg_1_{name_gen}", str_data)
    dpg.set_value(f"freg_2_{name_gen}", gen_data)


def analyze_data():
    """
    Анализ данных файла.
    """
    # Чтение файла и преобразование данных
    try:
        file_data = np.genfromtxt(dpg.get_value("file"), delimiter="\t", dtype=str)
        file_data = np.array(
            [float(elem.replace(",", ".").replace('"', "")) for elem in file_data]
        )
        dpg.set_value("text_file", "Успешно открыт и считан")
    except FileNotFoundError:
        print("Файл не найден")
        return
    except ValueError:
        print("Данные не могут быть преобразованы в чисал.")
        return
    except TypeError:
        print("Данные файла не являются строками.")
        return

    # Вычисление статистических характеристик
    dict_params = analysis.calculate_statistics(file_data)
    for key, value in dict_params.items():
        dpg.set_value(key, value)

    # Определение количества интервалов
    count_inter = round(5 * np.log10(dict_params["max"] - dict_params["min"]))
    dpg.set_value("count_range", count_inter)

    # Нахождение относительных частот исходных данных
    str_data = analysis.get_partition(file_data, count_inter)

    # Генерация данных
    norm, exp, gamma = analysis.number_generation(
        dict_params["mean"], dict_params["variance"], dict_params["count"] * 10
    )

    # Нахождение относительных частот сгенерированных данных
    norm = analysis.get_partition(norm, count_inter)
    exp = analysis.get_partition(exp, count_inter)
    gamma = analysis.get_partition(gamma, count_inter)

    # Отображение графиков
    add_data_plot("norm", str_data, norm)
    add_data_plot("exp", str_data, exp)
    add_data_plot("gamma", str_data, gamma)


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
                dpg.add_button(label="Analyze", callback=analyze_data)
                dpg.add_text("Сообщение о чтении файла: ")
                dpg.add_text("", tag="text_file")
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
                    tag="standard_deviation",
                    readonly=True,
                )
                dpg.add_input_text(label="Минимум", width=200, tag="min", readonly=True)
                dpg.add_input_text(
                    label="Максимум", width=200, tag="max", readonly=True
                )
            with dpg.group():
                with dpg.plot(
                    label="Нормальное распределение",
                    width=500,
                    height=300,
                    tag="plot_norm",
                ):
                    dpg.add_plot_legend()
                    dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis_norm")
                    dpg.add_line_series(
                        [],
                        [],
                        label="Исходная выборка",
                        tag="freg_1_norm",
                        parent="y_axis_norm",
                    )
                    dpg.add_line_series(
                        [],
                        [],
                        label="Норм. распр. выборка",
                        tag="freg_2_norm",
                        parent="y_axis_norm",
                    )
                with dpg.plot(
                    label="Гамма-распределение", width=500, height=300, tag="plot_gamma"
                ):
                    dpg.add_plot_legend()
                    dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis_gamma")
                    dpg.add_line_series(
                        [],
                        [],
                        label="Исходная выборка",
                        tag="freg_1_gamma",
                        parent="y_axis_gamma",
                    )
                    dpg.add_line_series(
                        [],
                        [],
                        label="Гамма-распр. выборка",
                        tag="freg_2_gamma",
                        parent="y_axis_gamma",
                    )
                with dpg.plot(
                    label="Экспоненциальное распределение",
                    width=500,
                    height=300,
                    tag="plot_exp",
                ):
                    dpg.add_plot_legend()
                    dpg.add_plot_axis(dpg.mvXAxis, label="Номер интервала")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Частота", tag="y_axis_exp")
                    dpg.add_line_series(
                        [],
                        [],
                        label="Исходная выборка",
                        tag="freg_1_exp",
                        parent="y_axis_exp",
                    )
                    dpg.add_line_series(
                        [],
                        [],
                        label="Эксп. распр. выборка",
                        tag="freg_2_exp",
                        parent="y_axis_exp",
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
