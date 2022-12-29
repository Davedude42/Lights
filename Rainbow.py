from Program import Program
import math

class Rainbow(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.speed = int(args[0]) if len(args) != 0 else 1 

	def frame(this, timer):
		for i in range(this.length):
			this.pixels[i] = (((i / this.length * 360) + (timer*this.speed)) % 360, 100, 50, 100)
			
		return True