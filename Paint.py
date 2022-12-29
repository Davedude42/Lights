from Program import Program
import useful
import time
import math
import colorsys

class Paint(Program):
	def __init__(this, length, args=[]):
		super().__init__(length)
		this.canvas = [(0, 0, 0, 0)]*length
		
		this.command = ''
		this.hasChanged = False
		
		this.selection = False
		
		this.cursor = 10
		this.ACTUALCursor = 10
		
		this.color = (0, 100, 50, 100)
		
		this.alsoCursor = 0
		
		this.shifted = False
		
		this.coloring = False
		this.changingColor = 0
	
	def frame(this, timer):
		if this.hasChanged:
			
			this.hasChanged = False
			return True
		else:
			return False

	def redraw(this):
		for i in range(this.length):
			this.pixels[i] = this.canvas[i]
			
		if this.selection:
			tempcolor = list(this.color[:]) if not this.shifted else [0, 0, 0, 0]
			tempcolor[3] = 100
			this.fillLine(tempcolor, this.alsoCursor, this.ACTUALCursor)
			this.pixels[useful.loop(this.alsoCursor, this.length)] = (0, 0, 100, 50)
			
		this.pixels[useful.loop(this.cursor, this.length)] = (0, 0, 100, 50)
		
		if this.coloring:
			i = 1
			summ = useful.WALLS[0]
			
			while summ < this.cursor and i < 4:
				summ += useful.WALLS[i]
				i += 1
			i %= 4
			useful.wall(this.pixels, i, (0, 0, 0, 100))
			length = useful.WALLS[i]
			oldColor = list(this.color)
			newColor = list(this.color)
			
			oldColor[this.changingColor] = 0
			newColor[this.changingColor] = 360 if this.changingColor == 0 else 100
			
			for j in range(1, length-1):
					this.pixels[useful.loop(summ + j, this.length)] = useful.gradient((oldColor, 0, newColor, 100), j/length*100)
			
			maxx = 360 if this.changingColor == 0 else 100
			this.pixels[useful.loop(1 + summ + math.floor((length-2)*this.color[this.changingColor]/maxx), this.length)] = (290, 100, 80, 100)
			
			
		this.hasChanged = True
		
	def key(this, k):
		print(k, this.command)
		
		if this.coloring:
			if k == 'enter':
				this.coloring = False
			elif k == 'up':
				this.changingColor += 1
				this.changingColor %= 4
			elif k == 'down':
				this.changingColor -= 1
				if this.changingColor < 0:
					this.changingColor += 4
			elif k == 'right':
				newcolor = list(this.color)
				newcolor[this.changingColor] +=   3 if this.changingColor == 0 else   1
				newcolor[this.changingColor] %= 360 if this.changingColor == 0 else 100
				this.color = tuple(newcolor)
			elif k == 'left':
				newcolor = list(this.color)
				newcolor[this.changingColor] -=   3 if this.changingColor == 0 else   1
				if newcolor[this.changingColor] < 0:
					newcolor[this.changingColor] += 360 if this.changingColor == 0 else 100
				this.color = tuple(newcolor)
			elif k == 'up':
				this.changingColor
		else:
			if k == 'shift':
				this.shifted = True
			if k == 'enter':
				if this.selection == False:
					this.canvas[this.cursor] = this.color if not this.shifted else (0, 0, 0, 0)
				elif this.selection == True:
					arr = useful.looping(this.ACTUALCursor, this.alsoCursor, this.length)
					for i in arr:
						this.canvas[useful.loop(i, this.length)] = this.color if not this.shifted else (0, 0, 0, 0)
					this.selection = False
			elif k == 'f':
				this.selection = True
				this.alsoCursor = this.ACTUALCursor
			elif k == 'w':
				i = 1
				summ = useful.WALLS[0]
				while summ < this.cursor and i < 4:
					summ += useful.WALLS[i]
					i += 1
				
				useful.wall(this.canvas, i-1, this.color if not this.shifted else (0, 0, 0, 0))
			
			elif k == 'a':
				for i in range(this.length):
					this.canvas[i] = this.color if not this.shifted else (0, 0, 0, 0)
			elif k == 'right':
				this.cursor = useful.loop(this.cursor+1, this.length)
				this.ACTUALCursor += 1
			elif k == 'left':
				this.cursor = useful.loop(this.cursor-1, this.length)
				this.ACTUALCursor -= 1
			elif k == 'c':
				this.coloring = True
			elif k == 'd':
				this.color = this.canvas[this.cursor]
			elif k.isnumeric():
				newcolor = list(list(useful.GOOD_COLORS.items())[int(k)-1][1])
				print(newcolor)
				newcolor[3] = this.color[3]
				this.color = tuple(newcolor)
		
		this.redraw()
		
	def keyUp(this, k):
		print("upppp", k)
		if k == 'shift':
			this.shifted = False
			this.redraw()
		