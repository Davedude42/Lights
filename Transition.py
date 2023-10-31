from Animation import Animation
import useful

class Transition(Animation):
	def __init__(this, oldPixels, newPixels):
		super().__init__(len(oldPixels))

		this.pixels = oldPixels.copy()

		this.oldPixels = oldPixels
		this.newPixels = newPixels
	
	def setPercent(this, p):
		super().setPercent(p)
		
		for i in range(len(this.pixels)):
			this.pixels[i] = useful.gradient((this.oldPixels[i], 0, this.newPixels[i], 100), this.percent)