#Programa unificado: Proyecto Final "Dispensador de comida para gatos" (sólo funciones de alto nivel)


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


from horario import hora_comida
from servo_control import abrir_compuerta, cerrar_compuerta
from menu_lcd import mostrar_menu
from hx711 import obtener_peso_actual # usando tu código HX711

TAMANIO = mostrar_menu()

while True:
  if hora_comida():
    peso_inicial = obtener_peso_actual()
    abrir_compuerta()
  while obtener_peso_actual() - peso_inicial < TAMANIO:
    time.sleep(0.5)
    cerrar_compuerta()
    time.sleep(60) # espera 1 minuto para evitar repetir
    time.sleep(1)