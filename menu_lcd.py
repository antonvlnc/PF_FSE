import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)
time.sleep(2)

def mostrar_mensaje(mensaje):
    mylcd.lcd_display_string(mensaje,1)