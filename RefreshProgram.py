from Program import Program
import math

class RefreshProgram(Program):
	def __init__(this, length, args):
		super().__init__(length)

	def frame(this, timer):
		if timer % (24 * 60 * 15) == 0:
			return True
		return False