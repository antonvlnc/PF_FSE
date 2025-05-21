# # menu_lcd.py
# from RPLCD.i2c import CharLCD
# import time

# lcd = CharLCD('PCF8574', 0x27)  # Dirección I2C común

# def mostrar_mensaje(texto, duracion=0):
#     """
#     Muestra un mensaje en la LCD. Limpia la pantalla antes de escribir.
#     Si el texto tiene '\n', escribe en ambas líneas.
#     """
#     lcd.clear()
#     lineas = texto.split("\n")
#     for i, linea in enumerate(lineas[:2]):  # Solo 2 líneas permitidas
#         lcd.cursor_pos = (i, 0)
#         lcd.write_string(linea.ljust(16)[:16])  # Asegura longitud correcta

#     if duracion > 0:
#         time.sleep(duracion)
#         lcd.clear()

import time
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()
second = 0

mylcd.lcd_display_string("FSE 2025-2", 1,3) 
mylcd.lcd_display_string("BRIGADA08 GPO.06", 2,0)
time.sleep(3) #3 second delay
mylcd.lcd_clear() #clear lcd


mylcd.lcd_display_string("MORALES MARTINEZ", 1,0)
mylcd.lcd_display_string("KARLA VERONICA", 2,0)
time.sleep(3) #create 3 second delay
mylcd.lcd_clear() #clear 1cd

mylcd.lcd_display_string("ROBLES JIMENEZ", 1,0)
mylcd.lcd_display_string("MARCO ANTONIO", 2,0)
time.sleep(3) #3 second delay
mylcd.lcd_clear() #clear 1cd

mylcd.lcd_display_string("TAPIA NAVARRO", 1,0)
mylcd.lcd_display_string("RODRIGO", 2,0)
time.sleep(3) #3 second delay
mylcd.lcd_clear() #clear 1cd

mylcd.lcd_display_string("TOLEDO VALENCIA", 1,0)
mylcd.lcd_display_string("JESUS ANTONIO", 2,0)
time.sleep(3) #3 second delay
mylcd.lcd_clear() #clear 1cd