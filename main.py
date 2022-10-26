from calc import Calc_block as c_calc
from logger import result_logger as write_log
import data_transformation as d_t
import console_ui as c_ui
import tg_bot as bot


def button_click():
    bot.start()
    j = d_t.data_formatting(c_ui.input_data())
    calc_result = c_calc(j)
    c_ui.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)


button_click()