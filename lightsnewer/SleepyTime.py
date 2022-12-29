from Program import Program
import useful
import math
import datetime

class SleepyTime(Program):
	def __init__(this, length, args):
		super().__init__(length)
		this.upTime = 315
		this.start = 0
		this.doing = "before"
		this.changed = False

	def frame(this, timer):
		if this.doing == "sleeping":
			if time % 24 == 0:
				time = datetime.datetime.now()
				if time.hour*60 + time.minute == this.upTime - 20:
					this.start = timer
				elif time.hour*60 + time.minute > this.upTime - 20:
					this.fill(useful.gradient(
						((9, 77, 16, 100), 0, (29, 100, 50, 100), 60, (190, 100, 90, 100), 100),
						(timer - this.start) / (24*60*20) * 100
					))
				elif time.hour*60 + time.minute > this.upTime:
					this.fill((255, 255, 255, 100))
				if time.hour*60 + time.minute >= this.upTime - 20:
					return True
		elif this.doing == "before":
			this.fill(useful.GOOD_COLORS["offer-white"])
			return True
		else:
			if this.changed:
				this.changed = False
				return True
			else:
				return False

	def key(this, k):
		if this.doing == "before":
			this.doing == "sleeping"
		elif this.doing == "sleeping":
			this.doing = "after"
		this.transition(this.pixels[0], (0, 0, 0, 0), 1)
		