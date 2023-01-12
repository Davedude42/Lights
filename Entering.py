from Program import Program
import time
class Entering(Program):
	def __init__(this, length, onCommand):
		super().__init__(length)
		
		this.commanding = False
		this.command = ''
		this.onCommand = onCommand
		this.hasChanged = False
	
	def frame(this, timer):
		if this.hasChanged:
			
			this.hasChanged = False
			return True
		else:
			return False

	def redraw(this, error=False):
		this.fill((0, 0, 0, 0))
		
		if this.commanding:
			this.fillLine((0, 100, 100, 60), 1, len(this.command) + 3)
			this.pixels[2] = (285, 100, 50, 70)
			for i, l in enumerate(this.command):
				if l != ' ':
					this.pixels[3 + i] = (0, 100, 50, 60) if error else (110, 100, 50, 60)
		
		
		this.hasChanged = True
		
	def key(this, k):
		
		if this.commanding == True:
			print('"'+k+'"')
			if k == 'space':
				this.command += ' '
			elif k == 'backspace':
				this.command = this.command[:-1]
			elif k == 'delete':
				this.command = ''
			elif k == 'esc':
				this.commanding = False
			elif k == 'enter':
				if this.command == '':
					this.commanding = False
					this.redraw()
					return
				com = this.command.split(' ')
				print("ran command:", this.command)
				if len(com) > 0:
					if com[0].isnumeric():
						comm = { 'key': com[1], 'layer': int(com[0]), 'args': com[2:] }
					else:
						comm = { 'key': com[0], 'layer': 10, 'args': com[1:] }
					
					res = this.onCommand(comm)
					if not res:
						this.redraw(True)
						time.sleep(0.6)
						# it redraws again later
					else:
						this.commanding = False
			elif isinstance(k, str) and len(k) == 1:
				this.command += k
			
		else:
			if k == '/':
				this.commanding = True
				this.command = ""
		this.redraw()
		