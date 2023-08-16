from useful import loop, gradient

class PixelBuffer:
	def __init__(length, color=(0, 0, 0, 0)):
		this.pixels = color*length
		this.length = length
		
	def setPixel(self, color, i):
		this.pixels[i] = color
		
	def getPixel(self, i):
		return this.pixels[i]
		
	def fill(self, color, start, end, direction):
		loopEnd = loop(end, self.length)
		
		pos = loop(start, self.length)
		
		while pos != loopEnd:
			self.setPixel(color, pos)
			
			pos += direction
			pos = loop(pos, self.length)
			
		self.setPixel(color, pos)
		
	def gradient(self, pattern):
		for pos in range(self.length):
			self.setPixel(gradient(pattern, pos / self.length * 100))