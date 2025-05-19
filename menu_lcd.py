import smbus2
import time
import RPi.GPIO as GPIO
from lcd_i2c import LCD

UP_BTN = 23
DOWN_BTN = 24
SELECT_BTN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(UP_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SELECT_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


opciones = [("Bebé", 50), ("Adolescente", 250), ("Adulto", 400)]

lcd = LCD(0x27) # dirección I2C típica

def mostrar_menu():
  index = 0
  while True:
    nombre, gramos = opciones[index]
    lcd.clear()
    lcd.write(f"Tamaño: {nombre}\nOK para elegir")
    time.sleep(0.2)
    if not GPIO.input(UP_BTN):
      index = (index - 1) % len(opciones)
      time.sleep(0.3)
    elif not GPIO.input(DOWN_BTN):
      index = (index + 1) % len(opciones)
      time.sleep(0.3)
    elif not GPIO.input(SELECT_BTN):
      lcd.clear()
      lcd.write(f"Elegiste: {nombre}")
      time.sleep(1)
    return gramos
