from Program import Program
import useful
import math
import datetime

from Animation import Animation
from Transition import Transition

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

		this.animation = None

		this.transitioning = False
		
		this.changeDoing("before", 0)

	def frame(this, timer):
		# transition
		if this.transitioning:
			this.animation.frame()
			this.pixels = this.animation.pixels

			this.changed = True

			if this.animation.transitionComplete():
				
				this.pixels = this.animation.pixels

				this.animation = None
				this.transitioning = False

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
						this.changeDoing('wakeup', 0)

		if this.changed:
			this.changed = False
			return True
		else:
			return False
	
	def key(this, k):
		if k == 'space':
			if this.doing == 'before':
				this.changeDoing('journal', 24)
			elif this.doing == 'journal':
				this.changeDoing('sleeping', 24*15)
			elif this.doing == 'sleeping':
				this.changeDoing('cantsleep', 24)
			elif this.doing == 'cantsleep':
				this.changeDoing('sleeping', 24)
		
	def changeDoing(this, newdoing, transitionDuration):
		this.doing = newdoing

		print('SleepyTime: I am now ' + this.doing)

		newPixels = [(0, 0, 0, 100)]*this.length

		if this.doing == 'before':
			this.isRGB = False

			newPixels = [useful.GOOD_COLORS["offer-white"]]*this.length

		if this.doing == 'journal':
			this.isRGB = False
			

			color = list(useful.GOOD_COLORS["offer-white"])
			color[3] = 50
			
			useful.wall(newPixels, 1, color)

		if this.doing == 'cantsleep':
			this.isRGB = False

			color = list(useful.GOOD_COLORS["offer-white"])
			color[3] = 20
			
			useful.wall(newPixels, 1, color)

		if this.doing == 'sleeping':
			this.isRGB = False

		if this.doing == 'wakeup':
			this.isRGB = False
			this.animation = Animation(this.length, ['wakeup', 0, False])

		else:
			this.transitioning = True
			this.animation = Transition(this.pixels, newPixels, transitionDuration)
		


