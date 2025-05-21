# menu_lcd.py
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)  # Dirección I2C común

def mostrar_mensaje(texto, duracion=0):
    """
    Muestra un mensaje en la LCD. Limpia la pantalla antes de escribir.
    Si el texto tiene '\n', escribe en ambas líneas.
    """
    lcd.clear()
    lineas = texto.split("\n")
    for i, linea in enumerate(lineas[:2]):  # Solo 2 líneas permitidas
        lcd.cursor_pos = (i, 0)
        lcd.write_string(linea.ljust(16)[:16])  # Asegura longitud correcta

    if duracion > 0:
        time.sleep(duracion)
        lcd.clear()
