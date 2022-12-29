import math
from useful import looping, loop, gradient
from time import sleep
class Program:
	def __init__(this, length, args=[]):
		this.pixels = [(0, 0, 0, 0)]*length
		this.length = length
		this.localTimer = 0
		this.changed = True
	
	def frame(this, timer):
		return False

	def key(this, k):
		pass
	
	def keyUp(this, k):
		pass

	def fill(this, color):
		if len(color) == 3:
			tempcolor = color + (100,)
		else:
			tempcolor = color
		
		this.pixels = [tempcolor]*this.length

	def fillLine(this, color, start, end):
		if len(color) == 3:
			tempcolor = color + (100,)
		else:
			tempcolor = color

		arr = looping(start, end, this.length)
		for i in arr:
			this.pixels[loop(i, this.length)] = tempcolor

	def transition(this, color1, color2, length):
		for time in range(0, length*24):
			this.fill(gradient(
				(color1, 0, color2, 100),
				time/(length*24)*100
			))
			this.changed = True
			sleep(1/24)