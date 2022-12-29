from colorPallete import colorPallete
import math
def combine(base, color, percent):
	return [base[i]+math.floor((color[i] - base[i])*(percent/100)) for i in range(3)]
class Paint(Program):
	def __init__(this, pixels, length, color):
		super(pixels, length)
		this.color = color - 1
		this.pxs = [(0, 0, 0) for i in range(length)]
		this.cursor = 10
		this.tool = 1
		this.toolSetting = 0
	def frame(this, timer):
		for i in range(this.length):
			this.pixels[i] = this.pxs[i]
		if this.tool == 1 or this.tool == 3:
			if (timer//24) % 2 == 0:
				this.pixels[this.cursor] = (100, 100, 100)
		if this.tool == 3 and this.toolSetting != -1:
			this.pixels[this.toolSetting] = (100, 100, 100)
			for i in range(math.min(this.cursor, this.toolSetting), math.max(this.cursor, this.toolSetting)):
					this.pixels[i] = combine(this.pixels[i], (255, 255, 255), 20)
	def key(this, k):
		if k == 'left':
			if this.tool == 3 and this.toolSetting != -1:
				this.toolSetting -= 1
				if this.toolSetting < 0:
					this.toolSetting += this.length
			else:
				this.cursor -= 1
				if this.cursor < 0:
					this.cursor += this.length
		elif k == 'right':
			if this.tool == 3 and this.toolSetting != -1:
				this.toolSetting += 1
				this.toolSetting %= this.length
			else:
				this.cursor += 1
				this.cursor %= this.length
		elif k == 'up':
			this.color += 1
			this.color %= len(colorPallete)
		elif k == 'down':
			this.color -= 1
			if this.color < 0:
				this.color += len(colorPallete)
		elif k.isnumeric() and int(k) >= 1 and int(k) <= 3:
			this.tool = int(k)
			if this.tool == 3:
				this.toolSetting = -1
		elif k == 'enter':
			if this.tool == 1:
				this.pxs[this.cursor] = colorPallete[this.color]
			elif this.tool == 3:
				for i in range(math.min(this.cursor, this.toolSetting), math.max(this.cursor, this.toolSetting)):
					this.pxs[i] = colorPallete[this.color]
				this.toolSetting = -1