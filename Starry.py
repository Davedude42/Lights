from Program import Program
import math
import random

class Starry(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.stars = []
		this.stars.append([random.randint(0, this.length-1), 0, random.randint(0, 359)])
		
		this.speed = int(args[0]) if len(args) != 0 else 5	
		

	def frame(this, timer):
		if timer % this.speed == 0:
			this.stars.append([random.randint(0, this.length-1), 0, random.randint(0, 359)])
			
		for i in range(len(this.stars)-1, 0, -1):
			star = this.stars[i]
			brightness = 30 * (-(star[1]*star[1]) + 50*star[1]) / (25*25)
			this.pixels[star[0]] = (star[2], 100, 90, brightness)
			
			star[1] += 1
			
			if star[1] > 50:
				this.stars.pop(i)
		return True
			