from Program import Program
import math

import socketio

# standard Python

class Interwebs(Program):
	def __init__(this, length, args):
		super().__init__(length)

		this.isRGB = True

		this.changed = True

		this.sio = socketio.Client()

		this.sio.connect('https://davidharoldsen.com')
		
		@this.sio.event
		def connect():
			print('connected 1')
			this.connect()
		@this.sio.on('initial')
		def initial(msg):
			this.updatePixels(msg["pixels"])
		@this.sio.on('pixelsToClient')
		def pixelsToClient(msg):
			this.updatePixels(msg["pixels"])

	def frame(this, timer):
		if this.changed:
			this.changed = False
			return True
		else:
			return False
	
	def connect():
		print('connected')

	def updatePixels(this, pxls):
		for i in range(this.length):
			this.pixels[i] = (pxls[i][0], pxls[i][1], pxls[i][2], 100)
		
		this.changed = True