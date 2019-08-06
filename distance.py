import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)

pinTrigger = 24
pinEcho = 23

# this function will be used to cleanup all pins when user interrupts the program
def close(signal, frame):
	# closing the ultrasonic program
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, close)

# setting up I/O pins
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
	GPIO.output(pinTrigger, True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

	startTime = time.time()
	stopTime = time.time()

	# listen for Echo pin and catch changes
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

	# calculate the accurate distance
	TimeElapsed = stopTime - startTime
	distance = (TimeElapsed * 34300) / 2

	print("Your size is ", dssd/len(diss), " cm")
	# wait 0.4s before sending signal again (can be changed of ignored)
	time.sleep(0.4)
