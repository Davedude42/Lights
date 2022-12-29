from PIL import Image

from Program import Program
import math

class Animation(Program):
	def __init__(this, length, args):
		super().__init__(length)
		try:
			this.img = Image.open("animations/" + args[0] + ".png").convert('RGB')
		except:
			this.img = None
		this.rate = 12
		this.frameLength = args[1]
		this.frameOn = 0

	def frame(this, timer):
		if timer / this.rate == timer // this.rate and this.img != None:
			for i in range(this.length):
				r, g, b = this.img.getpixel((i, this.frameOn))
				this.pixels[i] = (r, g, b, 100)
			this.frameOn += 1
			this.frameOn %= this.frameLength
			
			return True
			
		return False