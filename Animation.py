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
		this.rate = int(args[1]) if len(args) >= 2 else 12
		this.frameLength = this.img.size[1]
		this.frameOn = 0
		
		this.isRGB = True

		this.setFrame(0)

	def frame(this, timer):
		if this.rate != 0 and timer % this.rate == 0:
			this.advanceFrame()
		
			return True

		if this.changed:
			this.changed = False
			return True
		else:
			return False
		
	def setFrame(this, frame):
		this.frameOn = frame

		if this.img != None:
			for i in range(this.length):
				r, g, b = this.img.getpixel((i, this.frameOn))
				this.pixels[i] = (r, g, b, 100)

			this.changed = True

	def setPercent(this, percent):
		if percent > 1 or percent < 0:
			raise Exception("Animation percent out of range")
		
		this.setFrame(min(math.floor(percent * this.frameLength), this.frameLength-1))

	
	def advanceFrame(this):
		this.setFrame((this.frameOn + 1) % this.frameLength)