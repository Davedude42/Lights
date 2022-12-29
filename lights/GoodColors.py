from colorPallete import colorPallete
from Program import Program
import math
class GoodColors(Program):
	def __init__(this, pixels, length, color):
		super().__init__(pixels, length)
		this.color = color - 1
	def frame(this, timer):
		this.pixels.fill(colorPallete.values()[this.color])
	def key(this, k):
		try:
			if int(k) != 0 and int(k) <= 9:
				this.color = int(k-1)
		finally:
			pass
		if k == 'left' or k == 'down':
			this.color -= 1
			if this.color < 0:
				this.color += len(colorPallete)
		elif k == 'right' or k == 'up':
			this.color += 1
			this.color %= len(colorPallete)