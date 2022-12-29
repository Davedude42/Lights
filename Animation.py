from PIL import Image

from Program import Program
import math

class Animation(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.img = Image.open("animations/" + args[0] + ".png").convert('RGB')
		this.rate = 12
		this.frameLength = args[1]
		this.frameOn = 0

	def frame(this, timer):
		if timer / this.rate == timer // this.rate
			for i in range(this.length):
				r, g, b = this.img.getpixel((i, this.frameOn))
				this.pixels[i] = (r, g, b, 100)
			this.frameOn += 1
			this.frameOn %= this.frameLength
			
			return True
			
		return False