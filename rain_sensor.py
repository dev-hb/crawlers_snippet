import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

trigger = 23
echo = 24
led = 4

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(trigger, True)
while True:
  if GPIO.input(echo) == 0 :
    print("rain detected !")
    GPIO.output(led, True)
  else:
    GPIO.output(led, false)
  time.sleep(1)
