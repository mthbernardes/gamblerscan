#!/usr/bin/python
import socket,sys

#Checagem parametros
if len(sys.argv) < 2:
        print '[+] - Syntax Error'
        print '[+] - Usage: python '+sys.argv[0]+' host'
        print '[+] - Example:'
        print 'python '+sys.argv[0]+' www.facebook.com'
        exit()

#Funcao resolve host
def resolve(host):
	try:
		address = socket.gethostbyname(host)
		return address
	except:
		print '[+] - Impossivel resolver endereco'
		exit()
#Funcao scanner de portas
def scanner(address):
	c = 0
	for port in range(1,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		r = s.connect_ex((address,port))
		s.close()
		if r == 0:
			print '[+] - Porta',port,'aberta'
			c = c + 1
	return c

#Declaracao variaveis
dominio = sys.argv[1]
count = 0
#Main
try:
	ip = resolve(dominio)

	print '[+] - Executando varredura em %s / %s'%(dominio,ip)
	count = scanner(ip)
	print '[+] - Foram encontradas',count,'portas abertas'
	print '[+] - Execucao concluida com sucesso'

except KeyboardInterrupt:
	print
        print "[+] - Scaneamento Interrompido"
	print '[+] - Foram encontradas',count,'portas abertas antes da finalizacao do processo'
