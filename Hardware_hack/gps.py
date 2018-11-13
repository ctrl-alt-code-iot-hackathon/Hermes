from gps import *
import time
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
report = gpsd.next()
if report['class'] == 'TPV':
  lati=(getattr(report,'lat',0.0))
  longi=(getattr(report,'lon',0.0))
  print(lati)
  print(longi)
  s="lat:"+str(lati)+",lng:"+str(longi)
  print(s)
  time.sleep(1)
