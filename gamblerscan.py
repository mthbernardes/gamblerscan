#!/usr/bin/python
import socket,sys,argparse

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

if __name__ == "__main__":
	#Parser section
	parser = argparse.ArgumentParser()
	parser.add_argument("host",help="host to check doors")
	parser.add_argument("-m","--min",help="Port to start check",type=int)
	parser.add_argument("-M","--max",help="Port to finish check",type=int)
	args = parser.parse_args()
	
	#Variables
	count = 0
	
	#Main
	try:
		ip = resolve(args.host)
	
		print '[+] - Checking %s / %s'%(args.host,ip)
		count = scanner(ip)
		print '[+] - Found',count,'open doors'
		print '[+] - Completed successfully'
	
	except KeyboardInterrupt:
		print
	        print '[+] - Interrupted scan'
		print '[+] - Was found',count,'open doors before finish it'