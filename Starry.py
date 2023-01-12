from Program import Program
import math
import random

class Starry(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.stars = []
		

	def frame(this, timer):
		if timer % 30 == 0:
			this.stars.append([random.randint(0, length-1), 0, random.randint(0, 359)])
			
		for i in range(len(this.stars), 0, -1):
			star = this.stars[i]
			brightness = 50 * (-(star[1]*star[1]) + 200*star[1]) / (10000)
			this.pixels[star[0]] = (star[2], 100, 80, brightness)
			
			star[1] += 1
			
			if star[1] > 200:
				this.stars.pop(i)
			