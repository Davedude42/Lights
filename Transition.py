from Program import Program
import useful
import math

class Transition(Program):
	def __init__(this, oldPixels, newPixels, duration):
		super().__init__(len(oldPixels))

		this.pixels = oldPixels.copy()

		this.oldPixels = oldPixels
		this.newPixels = newPixels

		this.duration = duration

		this.time = 0
	
	def frame(this):

		percent = 0

		if this.time >= this.duration:
			percent = 100
		else:
			percent = this.time / this.duration * 100

		for i in range(this.length):
			this.pixels[i] = useful.gradient([this.oldPixels[i], 0, this.newPixels[i], 100], percent)

		this.time += 1

	def transitionComplete(this):
		return this.time >= this.duration