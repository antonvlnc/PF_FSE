import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()


def mostrar_mensaje(mensaje):
    mylcd.lcd_display_string(mensaje,1)