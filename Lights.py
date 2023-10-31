from threading import Thread
from useful import layer, hsl_to_rgb
import time
import math
from pynput.keyboard import Key, Listener

# from bluedot import BlueDot


from Rainbow import Rainbow
from Entering import Entering
from Paint import Paint
from Tint import Tint
from SleepyTime import SleepyTime
from Animation import Animation
from RefreshProgram import RefreshProgram
from Starry import Starry
from Interwebs import Interwebs

class Lights:
	def __init__(this, pixels):
		this.length = len(pixels)
		this.pixels = pixels
		
		"""this.bd = BlueDot(cols=2, rows=2)
		
		this.bd[0,0].color = 'black'
		this.bd[0,1].color = 'red'
		this.bd[1,1].color = '#cccccc'
		
		this.bd[1,0].visible = False
		
		this.bd[0,0].when_pressed = lambda: this.clearPrograms()
		this.bd[0,1].when_pressed = lambda: this.onCommand({ 'key': 'r', 'layer': 10, 'args': [] })
		this.bd[1,1].when_pressed = lambda: this.onCommand({ 'key': 'star', 'layer': 10, 'args': [1] })"""
		
		this.programs = {
			-1: RefreshProgram(this.length, []),
			1000: Entering(this.length, this.onCommand)
		}
		
		this.paused = False
		this.sleeping = False
		
		this.force = True
		
		this.FPS = 24
		
		this.timer = 0
		
		this.listen = Listener(
			on_press=this.keyPress,
			on_release=this.keyRelease)
		this.listen.start()
			
	
	def clearPrograms(this):
		for pkey in list(this.programs.keys()):
			if pkey < 1000:
				this.programs.pop(pkey, None)
		this.force = True
	
	def keyPress(this, k):
		
		try:
			key = k.char.lower()  # single-char keys
		except:
			key = k.name  # other keys
		
		if key == 'esc':
			this.clearPrograms()
		elif key == '`':
			this.setPaused(not this.paused)
			
		for k, program in sorted(this.programs.items()):
			res = program.key(key)
			if res == False:
				break
		
	def keyRelease(this, k):
		try:
			key = k.char.lower()  # single-char keys
		except:
			key = k.name  # other keys
		
		pros = list(this.programs.items()).copy()
		pros.reverse()
		for k, program in pros:
			res = program.keyUp(key)
			if res == False:
				break
		
	def onCommand(this, com):
		if com['key'] == 'r':
			this.programs[com['layer']] = Rainbow(this.length, com['args'])
		elif com['key'] == 'pop':
			this.programs.pop(int(com['layer']), None)
		elif com['key'] == 'p':
			this.programs[com['layer']] = Paint(this.length, com['args'])
		elif com['key'] == 't':
			this.programs[com['layer']] = Tint(this.length, com['args'])
		elif com['key'] == 'n':
			this.programs[com['layer']] = SleepyTime(this.length, com['args'])
		elif com['key'] == 'a':
			this.programs[com['layer']] = Animation(this.length, com['args'])
		elif com['key'] == 'star':
			this.programs[com['layer']] = Starry(this.length, com['args'])
		elif com['key'] == 'web':
			this.programs[com['layer']] = Interwebs(this.length, com['args'])
		else:
			return False
			
		this.force = True

		return True
		
	def begin(this, FPS=24):
		print("Here are the possible commands:")
		print("Rainbow - /r [speed]")
		print("Stop a program - /[layer] pop")
		print("Paint - /p")
		print("Nighttime - /n")
		print("Animation - /a [animation]")
		print("Starry - /star")
		this.FPS = FPS
		while not this.sleeping:
			this.frame()
			
			time.sleep(1/this.FPS)
		

	def frame(this):
		if not this.sleeping and not this.paused:
			
			this.fill((0, 0, 0, 0))
			
			anyUpdated = False
			for k, program in this.programs.items():
				res = program.frame(this.timer)
				anyUpdated = res or anyUpdated
			
			if anyUpdated or this.force:
				for k, program in sorted(this.programs.items()): # loop through programs
					for i in range(this.length): # loop through pixels
						pxl = list(program.pixels[i])
						if(program.isRGB):
							rgb = pxl
						else:
							rgb = hsl_to_rgb(pxl)
						this.pixels[i] = layer(this.pixels[i], rgb)
				this.pixels.show()
						
				this.force = False
			this.timer += 1
			
	def sleep(this):
		this.sleeping = True
		
	def wake(this):
		if this.sleeping == True:
			
			this.sleeping = False
			thread = Thread(target = this.begin, args = (this.FPS))
			thread.start()
			#thread.join()
				
	def setPaused(this, val):
		this.paused = val
		
	def fill(this, color):
		this.pixels.fill(color)
		
		