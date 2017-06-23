import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1Enable = 5
Motor1B = 24
Motor1A = 27

Motor2Enable = 17
Motor2B = 6
Motor2A = 22
#single shot script used as a warning shot
# Set up defined GPIO pins
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1Enable,GPIO.OUT) 

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2Enable,GPIO.OUT)

# Turn the firing motor on
GPIO.output(Motor2A,GPIO.HIGH) 
GPIO.output(Motor2B,GPIO.LOW) 
GPIO.output(Motor2Enable,GPIO.HIGH) 
# warm it up for half a second 
sleep(0.5)

#turn on firing mechanism
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1Enable,GPIO.HIGH) 

# Stop the motor
sleep(0.5)

GPIO.output(Motor2Enable,GPIO.LOW)
GPIO.output(Motor1Enable,GPIO.LOW)
# Always end this script by cleaning the GPIO
GPIO.cleanup()