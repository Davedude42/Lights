from Program import Program
import useful
import math
import datetime

from Animation import Animation

class SleepyTime(Program):
	def __init__(this, length, args):
		super().__init__(length)

		wakeUpTime = [5*60 + 5, 5*60 + 5, 5*60 + 5, 5*60 + 30, -1, -1, 5*60 + 5]
		
		day = datetime.datetime.now().weekday()
		if len(args)>0:
			if args[0].__contains__(':'):
				hour = int(args[0].split(':')[0])
				minute = int(args[0].split(':')[1])
				this.upTime = hour*60 + minute
			else:
				this.upTime = -1
		else:
			this.upTime = wakeUpTime[day]
		
		if this.upTime == -1:
			print('Not waking up')
		else:
			add0 = '0' + str(this.upTime%60) if this.upTime%60 < 10 else str(this.upTime%60)
			print("getting up at", str(this.upTime//60) + ':' + add0)

		# how long the wakeup animation takes
		this.wakeupDuration = 25

		this.wakeupStart = this.upTime - this.wakeupDuration
		
		this.counter = -1
		this.fill(useful.GOOD_COLORS["offer-white"])

		this.animation = None
		
		this.changeDoing("sleeping")

	def frame(this, timer):
		# only bother updating every half second
		if(timer % 12 == 0):
			date = datetime.datetime.now()
			time = date.hour * 60 + date.minute

			# make any updates

			if(this.doing == 'wakeup' and timer % 24 == 0):
				this.animation.setFrame(min(time - this.wakeupStart, this.wakeupDuration))
				this.pixels = this.animation.pixels

			# check if it's time for something

			# if in the morning, not in the evening
			if time < 12 * 60:
				if this.doing == 'sleeping':
					if time >= this.wakeupStart:
						this.changeDoing('wakeup')

		if this.changed:
			this.changed = False
			return True
		else:
			return False
	
	def key(this, k):
		pass
		
	def changeDoing(this, newdoing):
		this.doing = newdoing

		if(this.doing == 'sleeping'):
			this.isRGB = False
			this.fill((0, 0, 0, 100))
		if(this.doing == 'wakeup'):
			this.isRGB = True
			this.animation = Animation(this.length, ['wakeup', 0])


