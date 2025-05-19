import RPi.GPIO as GPIO
import time

SERVO_PIN = 18 # cambia si usas otro pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50) # 50 Hz
pwm.start(0)

def set_angle(angle):
  duty = 2 + (angle / 18)
  GPIO.output(SERVO_PIN, True)
  pwm.ChangeDutyCycle(duty)
  time.sleep(0.5)
  GPIO.output(SERVO_PIN, False)
  pwm.ChangeDutyCycle(0)

def abrir_compuerta():
  set_angle(90) # abre

def cerrar_compuerta():
  set_angle(0) # cierra

def cleanup_servo():
  pwm.stop()
  GPIO.cleanup()

