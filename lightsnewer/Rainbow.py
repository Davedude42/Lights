from Program import Program
import math
"""
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
	return (r, g, b, 100)"""

class Rainbow(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.speed = int(args[0]) if len(args) != 0 else 1 

	def frame(this, timer):
		for i in range(this.length):
			this.pixels[i] = (((i / this.length * 360) + (timer*this.speed)) % 360, 100, 50, 100)
			
		return True