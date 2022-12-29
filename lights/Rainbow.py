from Program import Program
import math

def wheel(pos):
	# Input a value 0 to 255 to get a color value.
	# The colours are a transition r - g - b - back to r.
	if pos < 0 or pos > 255:
		r = g = b = 0
	elif pos < 85:
		r = int(pos * 3)
		g = int(255 - pos * 3)
		b = 0
	elif pos < 170:
		pos -= 85
		r = int(255 - pos * 3)
		g = 0
		b = int(pos * 3)
	else:
		pos -= 170
		r = 0
		g = int(pos * 3)
		b = int(255 - pos * 3)
	return (r, g, b)

class Rainbow(Program):
	def __init__(this, length, speed):
		super().__init__(length)
		this.speed = speed
		this.update = True

	def frame(this, timer):
		for i in range(this.LENGTH):
			this.pixels[i] = wheel((math.floor(i / this.LENGTH * 256) + math.floor(timer*this.speed) % 256) % 256)