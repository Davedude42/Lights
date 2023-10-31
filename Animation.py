from Program import Program

class Animation(Program):
	percent = 0
	
	def __init__(this, length):
		super().__init__(length)
		
<<<<<<< HEAD
		this.isRGB = args[2] == True if len(args) >= 3 else True
		
		try:
			this.img = Image.open("animations/" + args[0] + ".png").convert('RGB' if this.isRGB else 'HSL')
		except:
			this.img = None
			
		this.rate = int(args[1]) if len(args) >= 2 else 12
		this.frameLength = this.img.size[1]
		this.frameOn = 0

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
				r, g, b = this.img.getpixel((i, min(this.frameLength, this.frameOn)))
				this.pixels[i] = (r, g, b, 100)

			this.changed = True

	def setPercent(this, percent):
		if percent > 1 or percent < 0:
=======
	def setPercent(this, p):
		if p > 100 or p < 0:
>>>>>>> 91ca780a51c48fb8f74870b6cccaa54ada6c0e0f
			raise Exception("Animation percent out of range")
		else:
			this.percent = p
		