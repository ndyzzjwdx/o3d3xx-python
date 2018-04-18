#/usr/bin/python3

from settings import *

import o3d3xx
import sys
import time

def main():
	if len(sys.argv) > 1:
		address = sys.argv[1]
	else:
		address = CAMERAIP
	print('IP:' + str(address))
	
	session = createSession(address)
	app = createApp(session)
	
def createSession(address):
	try:
		device = o3d3xx.Device(address)
		session = device.requestSession()
		session.startEdit()
	except:
		print('session cannot be created, you must choose an available camera IP.')
		sys.exit(1)
	print('session can be created.')
	return session
	
def createApp(session):
	try:
		applicationIndex = session.edit.createApplication()
		application = session.edit.editApplication(applicationIndex)
	except:
		print('application cannot be created, you must choose an available camera IP.')
		sys.exit(1)
	print('application can be created.')
	return application	
		
if __name__ == '__main__':
	main()