from Program import Program
import useful
import math
import datetime

from ImageAnimation import ImageAnimation
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

		this.animation = None

		this.transitioning = False
		this.transitionDuration = 0
		this.transitionStart = 0
		
		this.changeDoing("before", 0)

	def frame(this, timer):
		date = datetime.datetime.now()
		time = date.hour * 60 + date.minute + date.second/60 + date.microsecond/60/1000000
			
		# transition
		if this.transitioning:
			if this.transitionDuration == 0:
				this.animation.setPercent(100)
			else:
				this.animation.setPercent((time - this.transitionStart) / this.transitionDuration * 100)
			
			this.pixels = this.animation.pixels
			
			if time >= this.transitionStart + this.transitionDuration:
				this.transitioning = False

			return True
		else:
			
			# if in the morning, not in the evening
			if time < 12 * 60:
				if this.doing == 'sleeping' and time >= this.wakeupStart:
					this.changeDoing('wakeup', this.wakeupDuration)

		return False
	
	def key(this, k):
		if k == 'space':
			if this.doing == 'before':
				this.changeDoing('journal', 1/60)
			elif this.doing == 'journal':
				this.changeDoing('sleeping', 15/60)
			elif this.doing == 'sleeping':
				this.changeDoing('cantsleep', 1/60)
			elif this.doing == 'cantsleep':
				this.changeDoing('sleeping', 1/60)
			elif this.doing == 'wakeup':
				this.changeDoing('awakenow', 1/60)
		elif k == 'd':
			this.changeDoing('wakeup', 0)
			
			this.wakeupDuration = 1
			date = datetime.datetime.now()
			time = date.hour * 60 + date.minute
			this.wakeupStart = time

		
	def changeDoing(this, newdoing, transitionDuration):
		this.doing = newdoing

		print('SleepyTime: I am now ' + this.doing)
		
		date = datetime.datetime.now()
		time = date.hour * 60 + date.minute + date.second/60
				
		this.transitioning = True
		this.transitionDuration = transitionDuration
		this.transitionStart = time
		
		if this.doing == 'wakeup':
			this.animation = ImageAnimation(this.length, ['wakeup'])
		else:
			newPixels = [(0, 0, 0, 100)]*this.length
			
			if this.doing == 'before':
	
				newPixels = [useful.GOOD_COLORS["offer-white"]]*this.length
	
			if this.doing == 'journal':
	
				color = list(useful.GOOD_COLORS["offer-white"])
				color[3] = 50
				
				useful.wall(newPixels, 1, color)
	
			if this.doing == 'cantsleep':
	
				color = list(useful.GOOD_COLORS["offer-white"])
				color[3] = 20
				
				useful.wall(newPixels, 1, color)
	
			if this.doing == 'awakenow':
	
				color = list(useful.GOOD_COLORS["offer-white"])
				
				useful.wall(newPixels, 1, color)
				
			this.animation = Transition(this.pixels, newPixels)
		


