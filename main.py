#Programa unificado: Proyecto Final "Dispensador de comida para gatos" (sólo funciones de alto nivel)
import balanza
import servo_control
import menu_lcd
import horario
import time
import RPi.GPIO as GPIO
'''
Pseudocódigo (hacer un diagrama de flujo y agregarlo al repo):

Inicio
- Compuerta cerrada / display LCD en main menu / plato sin comida. La botella con el alimento debe estar cerca del plato por
    la comida que cae aunque el servo se active y se cierre rápido.

Será en función del tiempo    

Seleccion del tamaño del gato (Bebé, Adolescente, Adulto)
- Bebé = 50g
- Adolescente = 250g
- Adulto = 400g

'''
if horario.hora_comida():
    balanza.obtener_peso_actual()
    while balanza.obtener_peso_actual < 250.0:
        servo_control.abrir_compuerta()
        balanza.obtener_peso_actual()
        # Aquí se puede agregar un tiempo de espera para que el servo se cierre después de abrir la compuerta
        time.sleep(1)
    servo_control.cerrar_compuerta()

