import math
from useful import looping, loop, gradient
from time import sleep
class Program:
	def __init__(this, length, args=[]):
		this.pixels = [(0, 0, 0, 0)]*length
		this.length = length
		this.localTimer = 0
		this.changed = True

		this.isRGB = False
	
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

	def gradient(this, steps, start, end):
		arr = looping(start, end, this.length)
		for i, index in arr:
			this.pixels[loop(i, this.length)] = gradient(steps, 100*math.floor(index / len(arr)))

	def transition(this, color1, color2, length):
		for time in range(0, length*24):
			this.fill(gradient(
				(color1, 0, color2, 100),
				time/(length*24)*100
			))
			this.changed = True
			sleep(1/24)

	def slidingTransition(this, length, options):
		color1 = options.color1 or (0, 0, 0)
		color2 = options.color2 or (0, 0, 50)
		smoothLength = options.smoothLength or 10
		start = options.start or 0
		end = options.end or this.length
		
		for time in range(0, length*24):
			smoothStart = math.floor(start + ((end - start) + smoothLength) * (time / (length*24)))
			this.fillLine(color1, start, smoothStart)
			this.gradient((color1, 0, color2, 100), smoothStart, min(end, smoothStart + smoothLength))
			this.fillLine(color2, smoothStart, end)
			this.changed = True
			sleep(1/24)