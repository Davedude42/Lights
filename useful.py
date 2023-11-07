import math
WALLS = [110, 106, 109, 107]
WALLS_SUM = []
s = 0
for i in range(len(WALLS)):
	s += WALLS[i]
	WALLS_SUM.append(s)

def layer(base, top):
	return [math.floor(base[0] + (top[0] - base[0]) * (top[3]/100)),\
	math.floor(base[1] + (top[1] - base[1]) * (top[3]/100)),\
	math.floor(base[2] + (top[2] - base[2]) * (top[3]/100))]
	
import colorsys
def gradient(pattern, percent):
	i = 0
	while True:
		if i + 2 >= len(pattern):
			return pattern[i]
		elif percent < pattern[i+3]:
			p = (percent - pattern[i+1]) / (pattern[i+3]-pattern[i+1])
			return [pattern[i][j]+math.floor((pattern[i+2][j] - pattern[i][j])*p) for j in range(4)]
		i += 2

def hsl_to_rgb(hsl):
	color = colorsys.hls_to_rgb(hsl[0]/360, hsl[2]/100, hsl[1]/100)
	color = (math.floor(color[0]*255), math.floor(color[1]*255), math.floor(color[2]*255), hsl[3])
	return color

def rgb_to_hsl(rgb):
	color = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
	color = (math.floor(color[0]*360), math.floor(color[2]*100), math.floor(color[1]*100), rgb[3])
	return color

def wall(pixels, walln, color):
	start = sum(WALLS[:walln%4])
	for i in range(start, start+WALLS[walln%4]):
		pixels[i] = color
		
def loop(index, length):
	
	i = index
	while i < 0:
		i += length
	while i >= length:
		i -= length
	return i
def looping(start, end, length):
	ret = [start]
	i = start
	while i != end:
		i += 1 if end > start else -1
		ret.append(i)
	return ret

def loopedList(length, start, end):
	ret = []
	
	
GOOD_COLORS = {
	"red": (4, 95, 50, 100),
	"orange": (25, 100, 50, 100),
	"yellow": (46, 100, 50, 100),
	"green": (120, 95, 40, 100),
	"teal": (160, 100, 50, 100),
	"blue": (230, 100, 25, 100),
	"purple": (285, 100, 37, 100),
	"off-white": (20, 100, 65, 100),
	"offer-white": (20, 100, 55, 100),
	}