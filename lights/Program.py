class Program:
	def __init__(this, length):
		this.pixels = [(0, 0, 0, 0)]*length
		this.length = length
		this.localTimer = 0
		this.update = False
	
	def frame(this, timer):
		return False

	def key(this, k):
		pass

	def fill(this, color):
		if len(color) == 3:
			tempcolor = color + (100,)
		else:
			tempcolor = color
		
		this.pixels = [tempcolor]*this.length

	def fillLine(this, color, start, end):
		if len(color) == 3:
			tempcolor = color + (100,)
		else:
			tempcolor = color

		for i in range(start, end):
			this.pixels[i] = tempcolor