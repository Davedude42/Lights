from Program import Program
import math
import useful

class FPS(Program):
	def __init__(this, length, args):
		super().__init__(length)
		
		this.previousTime = time.time()
		
		this.targetFPS = args[0] if len(args) > 0 else 24
		

	def frame(this, timer):
		time = time.time()
		
		FPS = 1/(time - this.previousTime)
		
		this.fillLine((0, 0, 100), 0, 26)
		this.fillLine(useful.GOOD_COLORS.green, 1, 1 + math.floor(FPS/this.targetFPS*24))
		
		this.previousTime = time
		
		return True