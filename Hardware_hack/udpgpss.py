import socket
UDP_IP_ADDRESS="192.168.137.26"
UDP_PORT_NO=23909
serversock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))
while True:
	data,addr=serverSock.recvfrom(23909)
	print "THE DATA IS",data
