import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
duty=0
p = GPIO.PWM(2, 50) # channel=12 frequency=50Hz
p.start(0)
p.ChangeDutyCycle(100)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 1)
GPIO.output(3, 1)
try:
	while 1:
		if not GPIO.input(17):
			if duty==0:
				duty=100
		else: duty=duty-10
		p.ChangeDutyCycle(duty)
		time.sleep(0.1)
	except KeyboardInterrupt:
		pass
	p.stop()
	GPIO.cleanup()