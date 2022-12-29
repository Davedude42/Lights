from Program import Program
import time
class Entering(Program):
	def __init__(this, length, onCommand):
		super().__init__(length)
		
		this.update = False
		this.commanding = False
		this.command = ''
		this.onCommand = onCommand
		this.error = False
	
	def frame(this, timer):
		this.fill((0, 0, 0, 0))

		this.fillLine((255, 255, 255, 10), 1, len(this.command) + 3)
		for i, l in enumerate(this.command):
			if l != ' ':
				this.pixels[2 + i] = (255, 50, 50, 40) if this.error else (50, 255, 50, 30)

		this.update = False


	def key(this, k):
		if this.commanding == True:
			if k == 'space':
				this.command += ' '
			elif k == 'backspace':
				this.command = this.command[:-1]
			elif k == 'delete':
				this.command = ''
			elif k == 'enter':
				com = this.command.split(' ')
				if len(com) > 0:
					if com[0].isnumeric():
						comm = { 'key': com[1], 'layer': int(com[0])-1, 'args': com[2:] }
					else:
						comm = { 'key': com[0], 'layer': 0, 'args': com[1:] }
					
					res = this.onCommand(comm)
					this.commanding = False
					if res == False:
						this.error = True
						this.update = True
						time.sleep(0.6)
						this.error = False
						this.command = ''
						this.update = True

			elif len(k) == 1:
				this.command += k
		else:
			if k == '/':
				this.commanding = True
		print(k, this.command)

		this.update = True
