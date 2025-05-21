import RPi.GPIO as GPIO
import time

SERVO_PIN = 18  # Cambia si usas otro pin


GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # Frecuencia: 50 Hz

def abrir_compuerta():
    pwm.start(7.5)  # Posición inicial (centro)
    time.sleep(1)  # Espera para estabilizar
    pwm.ChangeDutyCycle(10)  # Mueve el servo
    time.sleep(1)  # Espera para que el servo se mueva


    pwm.ChangeDutyCycle(10)  # Mueve el servo
    time.sleep(1)  # Espera para que el servo se mueva

try:
    pwm.start(7.5)  # Posición inicial (centro)
    time.sleep(1)  # Espera para estabilizar

    pwm.ChangeDutyCycle(10)  # Mueve el servo
    time.sleep(1)  # Espera para que el servo se mueva

    pwm.ChangeDutyCycle(0)  # Detiene el servo
finally:
    pwm.stop()  # Detiene el PWM
    GPIO.cleanup()  # Limpia la configuración de GPIO