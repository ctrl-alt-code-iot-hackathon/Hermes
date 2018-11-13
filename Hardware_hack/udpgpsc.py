from gps import *
import socket
import time
UDP_IP_ADDRESS="192.168.137.26"
UDP_PORT_NO=23909
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
report = gpsd.next()
if report['class'] == 'TPV':
  lati=(getattr(report,'lat',0.0))
  longi=(getattr(report,'lon',0.0))
  print(lati)
  print(longi)
  s="lat:"+str(lati)+",lng:"+str(longi)
 # print(s)
  time.sleep(1)
clientSock=socket.socket(socket.AF_Inet,socket.SOCK_DGRAM)
clientSock.sendto(s,(UDP_IP_ADDRESS,UDP_PORT_NO))
