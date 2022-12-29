from Program import Program
import math

from useful import gradient

class Tint(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.first = True

	def frame(this, timer):
		for i in range(this.length):
			this.pixels[i] = gradient(((0, 0, 0, 0), 0, (255, 255, 255, 100), 100), i/this.length*100)
		
		ret = this.first
		this.first = False
		return this.first
