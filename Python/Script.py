#! /usr/bin/python

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#--Copyright 2014 Sebastian Ortiz                                   #
#--This program is free software: you can redistribute it and/or    #
#--modify it under the terms of the GNU General Public License as   #
#--published by the Free Software Foundation, either version 3 of   #
#--the License, or (at your option) any later version.              #
#--                                                                 #
#--This program is distributed in the hope that it will be useful,  #
#--but WITHOUT ANY WARRANTY; without even the implied warranty of   #
#--MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the    #
#--GNU General Public License for more details.                     #
#--                                                                 #
#--You should have received a copy of the GNU General Public License#
#--along with this program.                                         #
#--If not, see <http://www.gnu.org/licenses/>.                      #
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#--Script.py                                                        #
#--Version: V1.1                                                    #
#--Serial-Html Bridge                                               #
#--This script serves to communicate a Front-End Web Application    #
#--With a Serial Device                                             #
#--By: Sebastian Ortiz, Electronic Engineering Student              #
#--Universidad de Antioquia - Colombia                              #
#--                                                                 #
#--Date:10/02/2014 17:50                                            #
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#--Blocks design:                                                   #
#--    __________             __________              __________    #
#--   |          | WebSocket |          | Serial Com |          |   #
#--   |Web App   |---------->|Script    |----------->|Device    |   #
#--   |__________|<----------|__________|<-----------|__________|   #
#--                                                                 #
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#

import sys
import getopt
import serial
import threading
import os
import time
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

fin = 0
Puerto = 16
connection = 0
s = 0

class SimpleSend(WebSocket):

	def handleMessage(self):
		if self.data is None:
			self.data = ''
		# echo message back to client
		#self.sendMessage(str(self.data))
		a = self.data
		print a
		writer(a)
		
	def handleConnected(self):
		global connection
		print self.address, 'connected'
		connection = 1

	def handleClose(self):
		print self.address, 'closed'
		connection = 0
	

def writer(ans):
		s.write(ans)

def reader():
#-- Cuando fin=1 se termina el thread
	global connection
	while not(fin):
		try:
			data = s.read()
			if data == '':
				pass
			else:
				sys.stdout.write(data)
				if connection == 1:
					server.send(data)
				else:
					print "Web App not detected"
				sys.stdout.flush()
				info = data
		except:
			print "Excepcion: Abortando..."
			break;

def webconnect():
	server.serveforever()

def serialconnect(Port,Vel):
	global s
	try:
		s = serial.Serial(Port, Vel)
		#-- Timeout: 1 seg
		s.timeout=1;
   
	except serial.SerialException:
		#-- Error al abrir el puerto serie
		sys.stderr.write("Error al abrir puerto: " + str(Puerto))
		sys.exit(1)

		
server = SimpleWebSocketServer('', 9876, SimpleSend)

w = threading.Thread(target=webconnect)
w.start()

time.sleep(1)
		
serialconnect(Puerto,9600)		
print ("Puerto serie (%s): %s") % (str(Puerto),s.portstr) 
 
time.sleep(1)
 
#-- Lanzar el hilo que lee del puerto serie y saca por pantalla
r = threading.Thread(target=reader)
r.start()


while 1:
	pass