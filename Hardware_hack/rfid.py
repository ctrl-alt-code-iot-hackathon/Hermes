import serial                                                  #import serial module

   ser = serial.Serial ("/dev/ttyAMA0")                           #Open named port 
   ser.baudrate = 9600                                            #Set baud rate to 9600
   data = ser.read(12)
   print "hello"                                            #Read 12 characters from serial port to data
  # ser.close ()                                                   #Close port             
