from Program import Program
import math
def gradient(pattern, percent):
	i = 0
	while True:

		
		if i + 2 >= len(pattern):
			return pattern[i]
		elif percent < pattern[i+3]:
			p = (percent - pattern[i+1]) / (pattern[i+3]-pattern[i+1])
			return [pattern[i][j]+math.floor((pattern[i+2][j] - pattern[i][j])*p) for j in range(3)]
		i += 2

class Morning(Program):
	def __init__(this, pixels, length):
		this.pixels = pixels
		this.LENGTH = length

	def frame(this, timer):
		this.localTimer += 1
		this.pixels.fill(gradient(((50, 10, 0), 0, (255, 160, 100), 100), this.localTimer/(24*15)))