from PIL import Image

from Animation import Animation
import math

# @param Animation Name

class ImageAnimation(Animation):
	def __init__(this, length, args):
		super().__init__(length)
		
		this.name = args[0] if len(args) > 0 else ''
		
		this.nframes = 1
		this.frame = 0
		
		try:
			this.img = Image.open("animations/" + this.name + ".png").convert('rgb')
			this.nframes = this.img.size[1]
		except:
			this.img = None
			print("Couldn't load animation '" + this.name + "'")
		
	def setFrame(this, frame):
		if frame > 100 or frame < 0:
			raise Exception("Animation percent out of range")
			
		this.frame = frame

		if this.img != None:
			for i in range(this.length):
				
				h, s, l = useful.rgb_to_hsl(this.img.getpixel((i, this.frame)))
				this.pixels[i] = (h, s, l, 100)

			this.changed = True

	def setPercent(this, percent):
		super().setPercent(percent)
		
		this.setFrame(min(math.floor(this.percent/100 * this.nframes), this.nframes-1))
