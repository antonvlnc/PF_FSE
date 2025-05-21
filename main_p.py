import balanza
import servo_control
import menu_lcd
import horario
import time
import RPi.GPIO as GPIO

# Selección del tamaño del gato → cambiar desde el menú
PESO_OBJETIVO = 250.0  # gramos

# Límite de intentos para evitar bucles infinitos
MAX_INTENTOS = 20
INTENTO_DELAY = 1  # segundos entre intentos

def servir_comida(peso_deseado):
    intentos = 0

    while True:
        peso_actual = balanza.obtener_peso_actual()
        print(f"Peso actual: {peso_actual}g")  # Opcional: mostrar en consola

        if peso_actual >= peso_deseado:
            print("✅ Peso suficiente, cerrando compuerta.")
            break

        if intentos >= MAX_INTENTOS:
            print("⚠️ Límite de intentos alcanzado. Comida no servida completamente.")
            break

        print("🔄 Abriendo compuerta para servir más comida.")
        servo_control.abrir_compuerta()
        time.sleep(0.5)  # Tiempo que se mantiene abierta
        servo_control.cerrar_compuerta()

        time.sleep(INTENTO_DELAY)
        intentos += 1

    servo_control.cerrar_compuerta()

# if __name__ == "__main__":
#     if horario.hora_comida():
#         menu_lcd.mostrar_mensaje("Hora de comer")
#         servir_comida(PESO_OBJETIVO)
#         menu_lcd.mostrar_mensaje("Comida lista 😺")
#     else:
#         menu_lcd.mostrar_mensaje("Esperando hora...")


if __name__ == "__main__":
    menu_lcd.mostrar_mensaje("Hora de comer")
    time.sleep(2)
    try:
        while True:
            if horario.hora_comida():
                menu_lcd.mostrar_mensaje("Hora de comer")
                servir_comida(PESO_OBJETIVO)
                menu_lcd.mostrar_mensaje("Comida lista 😺")
                time.sleep(600)  # Esperar 10 minutos antes de volver a revisar
            else:
                menu_lcd.mostrar_mensaje("Esperando hora...")
                print("Esperando la hora de la comida...")
                time.sleep(30)  # Espera
    except KeyboardInterrupt:
        print("\n🛑 Programa detenido por el usuario.")
        GPIO.cleanup()
