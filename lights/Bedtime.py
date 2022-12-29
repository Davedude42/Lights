from colorPallete import colorPallete
from Program import Program
import math
import datetime
import time

def gradient(pattern, percent):
	i = 0
	while True:
		if i + 2 >= len(pattern):
			return pattern[i]
		elif percent < pattern[i+3]:
			p = (percent - pattern[i+1]) / (pattern[i+3]-pattern[i+1])
			return [pattern[i][j]+math.floor((pattern[i+2][j] - pattern[i][j])*p) for j in range(3)]
		i += 2

class Bedtime(Program):
	def __init__(this, length, hour, minute):
		super().__init__(length)
		this.wakeup = hour * 60 + minute
		this.waiting = True
		this.light = True
		this.transition = False
		this.start = ()
		this.end = ()

		while this.waiting:
			now = datetime.datetime.now()
			if now.hour * 60 + now.minute >= this.wakeup - 20:
				this.waiting = False
				this.localTimer = 0
			time.sleep(60)


	def startTransition(this, end):
		this.transition = True
		this.start = this.pixels[0]
		this.end = end
	def frame(this, timer):
		if this.transition:
			this.fill(gradient((this.start, 0, this.end, 100), this.localTimer/(24*3)*100))
		else:
			if this.waiting == False:
				pattern = ((0, 0, 0), 0, (30, 10, 0), 40, (255, 255, 255), 100)
				this.fill(gradient(pattern, this.localTimer/(24*60*20)*100))
				this.update = True
			else:
				this.update = False
		
	def key(this, k):
		if this.light:
			print('turning off')
			if(k != 'b'):
				time.sleep(10)
			this.light = False
			this.startTransition((0, 0, 0))
		else:
			print('turning on')
			this.light = True
			this.startTransition(colorPallete['yellow-white'])
		this.update = True