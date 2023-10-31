from Program import Program

class Animation(Program):
	percent = 0
	
	def __init__(this, length):
		super().__init__(length)
		
	def setPercent(this, p):
		if p > 100 or p < 0:
			raise Exception("Animation percent out of range")
		else:
			this.percent = p
		