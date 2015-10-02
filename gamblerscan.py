#!/usr/bin/python
import socket,sys

#Param parser
if len(sys.argv) < 2:
        print '[+] - Syntax Error'
        print '[+] - Usage: python '+sys.argv[0]+' host'
        print '[+] - Example:'
        print 'python '+sys.argv[0]+' www.facebook.com'
        exit()

#Host resolve function
def resolve(host):
	try:
		address = socket.gethostbyname(host)
		return address
	except:
		print '[+] - Address resolve isn\'t possible'
		exit()
#Port scan function
def scanner(address):
	c = 0
	for port in range(1,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		r = s.connect_ex((address,port))
		s.close()
		if r == 0:
			print '[+] - Port',port,'is open'
			c = c + 1
	return c

#Variables
dominio = sys.argv[1]
count = 0
#Main
try:
	ip = resolve(dominio)

	print '[+] - Checking %s / %s'%(dominio,ip)
	count = scanner(ip)
	print '[+] - Found',count,'open doors'
	print '[+] - Completed successfully'

except KeyboardInterrupt:
	print
        print '[+] - Interrupted scan'
	print '[+] - Was found',count,'open doors before finish it'
