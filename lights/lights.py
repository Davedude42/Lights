import time
#import board
from pynput import keyboard
#import neopixel

import math

from Program import Program
from Rainbow import Rainbow
from GoodColors import GoodColors
from Bedtime import Bedtime
from Entering import Entering



LENGTH = 30*5*3-18
"""
pixel_pin = board.D21
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(
	pixel_pin, LENGTH, brightness=0.25, auto_write=False, pixel_order=ORDER
)"""
pixels = [(0, 0, 0)]*LENGTH
# --- remove

def processCommand(com):
	global programs

	nargs = len(com['args'])
	if com['key'] == 'd':
		programs.pop(com['layer'])
	if com['key'] == 'r':
		programs['inside'][com['layer']] = Rainbow(LENGTH, float(com['args'][0]) if nargs > 0 else 1)

	elif com['key'] == 'c':
		programs['inside'][com['layer']] = GoodColors(LENGTH, int(com['args'][0]) if nargs > 0 else 1)

	elif com['key'] == 'bed':
		programs['inside'][com['layer']] = Bedtime(LENGTH, int(com['args'][0]) if nargs > 0 else 5, int(com['args'][0]) if nargs > 0 else 10)

	else:
		return False

# has to be in this order
programs = {
	"under": [],
	"inside": {},
	"over": [Entering(LENGTH, processCommand)]
}

timer = 0
FPS = 24
running = True
forceStopFrame = False

#pixels = [0 for i in range(LENGTH)] # --- remove
		
def on_press(key):
	global running, pixels, enteringCommand, command, programs
	try:
		k = key.char  # single-char keys
	except:
		k = key.name  # other keys
	if k == 'space':
		changeRunning(not running)
	elif k == 'escape':
		programs['inside'] = {}
	else:
		programsFlat = [item for sublist in programs.values() for item in sublist]
		for pro in programsFlat:
			pro.key(k)


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()



#rgb 255 100 50
def wall(walln, color):
	lengths = [110, 106, 109, 107]
	start = sum(lengths[:walln%4])
	for i in range(start, start+lengths[walln%4]):
		pixels[i] = color
	 
def gradient(pattern, percent):
	i = 0
	while True:
		if i + 2 >= len(pattern):
			return pattern[i]
		elif percent < pattern[i+3]:
			p = (percent - pattern[i+1]) / (pattern[i+3]-pattern[i+1])
			return [pattern[i][j]+math.floor((pattern[i+2][j] - pattern[i][j])*p) for j in range(3)]
		i += 2

def layer(base, top):
	return [math.floor(base[i] + (top[i] - base[i]) * (top[3]/100)) for i in range(3)]

def changeRunning(run):
	global running, forceStopFrame

	if(running != run):
		running = run
		if running == True:
			frame()
		else:
			forceStopFrame = True

def frame():
	global programs, pixels, timer, forceStopFrame
	
	programsFlat = [item for sublist in programs.values() for item in sublist]

	anyUpdated = False
	for pro in programsFlat:
		if pro.update == True:
			pro.frame(timer)
		anyUpdated = pro.update or anyUpdated
	
	if(anyUpdated == True):
		#pixels.fill((0, 0, 0))
		for pro in programsFlat:
			if pro.update == True:
				for i in range(LENGTH):
					pixels[i] = layer(pixels[i], pro.pixels[i])
		#pixels.show()

	if(running):
		timer += 1
		time.sleep(1/FPS)
		if forceStopFrame == False:
			frame()
		else:
			forceStopFrame = False
		


frame()