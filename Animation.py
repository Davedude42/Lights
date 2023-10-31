from Program import Program

class Animation(Program):
	percent = 0
	
	def __init__(this, length):
		super().__init__(length)
		
	def setPercent(this, p):
		this.percent = min(p)
		