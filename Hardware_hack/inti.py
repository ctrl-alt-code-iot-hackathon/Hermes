import RPi.GPIO as GPIO
import SimpleMFRC522
from gps import *
import time
from websocket import create_connection
from time import sleep
ws=create_connection("ws://192.168.43.215:5002")

while True:
	gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
	report = gpsd.next()
	if report['class'] == 'TPV':
  	lati=(getattr(report,'lat',0.0))
  	longi=(getattr(report,'lon',0.0))
	lati=12.82686
	longi=80.04356
	s=str(lati)+","+str(longi)
	time.sleep(1)
	reader = SimpleMFRC522.SimpleMFRC522()
	id, text = reader.read()
	ws.send(s+","+text)
	sleep(1)
	GPIO.cleanup()
ws.close()










