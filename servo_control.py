import RPi.GPIO as GPIO
import time

SERVO_PIN = 18  # Cambia si usas otro pin


GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # Frecuencia: 50 Hz

def abrir_compuerta():

    pwm.ChangeDutyCycle(7.5)  # Mueve el servo
    time.sleep(1)  # Espera para que el servo se mueva

    # try:

    #     pwm.ChangeDutyCycle(10)  # Mueve el servo
    #     time.sleep(1)  # Espera para que el servo se mueva
       
    # except anything as e:
    #     print("Error al abrir la compuerta")
    #     pwm.ChangeDutyCycle(0)  # Detiene el servo
    #     time.sleep(1)  # Espera para estabilizar
    
def cerrar_compuerta():     
    pwm.ChangeDutyCycle(10)  # Detiene el servo
    time.sleep(1)  # Espera para estabilizar




