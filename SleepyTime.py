from Program import Program
import useful
import math
import datetime

class SleepyTime(Program):
	def __init__(this, length, args):
		super().__init__(length)
		
		day = datetime.datetime.today().weekday()
		if len(args)>0:
			if args[0].__contains__(':'):
				hour = int(args[0].split(':')[0])
				minute = int(args[0].split(':')[1])
				this.upTime = hour*60 + minute
			else:
				this.upTime = -1
		else:
			if day <= 3:
				this.upTime = 5*60 + 5
			elif day == 4:
				this.upTime = 5*60 + 30
			else:
				this.upTime = -1
		
		if this.upTime == -1:
			print('Not waking up')
		else:
			add0 = '0' + str(this.upTime%60) if this.upTime%60 < 10 else str(this.upTime%60)
			print("getting up at", str(this.upTime//60) + ':' + add0)
		
		this.time = -1
		this.doing = "before"
		this.changed = False
		this.fill(useful.GOOD_COLORS["offer-white"])
		this.dur = 20
		
		this.doingAfter = ""
		this.oldPixels = []
		this.newPixels = []
		this.transDur = 0

	def frame(this, timer):
		if this.doing == "sleeping":
			if timer % 24 == 0:
				time = datetime.datetime.now()
				if time.hour > 12 or this.upTime == -1:
					return False
				if this.time != -1:
					if this.time/60 < this.dur:
						this.fill(useful.gradient(
							((9, 77, 16, 100), 0, (29, 70, 50, 100), 60, (190, 100, 90, 100), 100),
							(this.time) / (60*this.dur) * 100
						))
					elif this.time/60 > this.dur + 15:
						if (this.time) % 2:
							this.fill((0, 100, 100, 100))
						else:
							this.fill((309, 100, 50, 100))
					else:
						this.fill((0, 100, 100, 100))
					this.time += 1
					return True
				elif time.hour*60 + time.minute == this.upTime - this.dur:
					print("It's time.")
					this.time = 0
			return False
		elif this.doing == "trans":
			for i in range(this.length):
				last = useful.gradient((this.oldPixels[i], 0, this.newPixels[i], 100), (this.time / this.transDur) * 100)
				this.pixels[i] = last
			this.time += 1
			if this.time > this.transDur:
				this.time = -1
				this.doing = this.doingAfter
				print("now doing: ", this.doing)
			return True
		else:
			if this.changed:
				this.changed = False
				return True
			else:
				return False

	def key(this, k):
		if this.doing == "before":
			
			old = this.pixels[:]
			
			this.fill((0, 0, 0, 0))
			color = list(useful.GOOD_COLORS["offer-white"])
			color[3] = 40
			useful.wall(this.pixels, 1, color);
			
			this.trans(old, "journal", 1)
			
		elif this.doing == "journal":
			old = this.pixels[:]
			
			this.fill((0, 0, 0, 0))
			
			this.trans(old, "sleeping", 20)
			
		elif this.doing == "sleeping":
			
			old = this.pixels[:]
			
			this.fill((0, 0, 0, 0))
			color = list(useful.GOOD_COLORS["off-white"])
			color[3] = 100
			useful.wall(this.pixels, 1, color);
			
			this.trans(old, "after", 1)
			
			
		
		#this.fill((0, 0, 0, 0))
	def trans(this, oldPixels, doing, length):
		this.time = 0
		this.doingAfter = doing
		this.oldPixels = oldPixels[:]
		this.newPixels = this.pixels[:]
		this.transDur = length * 24
		this.doing = "trans"
		
		