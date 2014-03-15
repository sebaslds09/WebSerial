

Communication System Web-Serial

This app is made to communicate a serial device with a web page and interchange
information. This approach the websocket system of HTML5 and websocket Lib in 
python to make a bridge between the web page and the computer and with de serial
device.
This is useful when you need realize some task in an secure environment like a server
side.

To RUN:

1) You can use a serial device like a microcontroller, or else. With the communication
function to send and receive strings. Also you can emulate a serial device with VSPE
or other software and the hyperterminal.

2) By default the Serial port and the Baud rate are: Com17/9600. if you want change it
you can change the values in ./Python/Scrypt.py :
	port Com(X-1) Line 34 -> Puerto = 16
	Baud Rate Line 105 -> serialconnect(Puerto,9600)
	
	If you are going to emulate the serial port, create a new connection in port com17
	and then run Hyperterminal

2) Run ./Python/Scrypt.py

3) Run ./html/index.html

All is ready, you can send and receive messages from the web page and from the serial device
or hyperterminal.  