from Lights import Lights
from tkinter import *
from math import *

from useful import WALLS, WALLS_SUM

LENGTH = 30*5*3-18

PIXEL_SIZE = 4

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

class FakePixels:
	def __init__(this, length):
		this.length = length
		this.pixels = [(0, 0, 0)]*this.length

		this.window = Tk()
		this.window.lift()
		this.canvas = Canvas(this.window, width = WALLS[0] * PIXEL_SIZE + 50, height = WALLS[1] * PIXEL_SIZE + 50)

		this.canvas.pack()

		this.canvas.configure(bg='#222222')

		this.pixelRects = []

		for i in range(this.length):
			px = 0
			py = 0

			for pi in range(i):
				if(pi < WALLS_SUM[0]):
					px += PIXEL_SIZE
				elif(pi < WALLS_SUM[1]):
					py += PIXEL_SIZE
				elif(pi < WALLS_SUM[2]):
					px -= PIXEL_SIZE
				elif(pi < WALLS_SUM[3]):
					py -= PIXEL_SIZE

				if pi == WALLS_SUM[2]:
					px -= PIXEL_SIZE
					py += PIXEL_SIZE

			rect = this.canvas.create_rectangle(25 + px, 25 + py, 25 + px + PIXEL_SIZE, 25 + py + PIXEL_SIZE, fill='#000000', outline="")
			this.pixelRects.append(rect)

	def __getitem__(this, index):
		return this.pixels[index]
	def __setitem__(this, index, color):
		#if(len(color) == 4):
		#	print('NO ALPHA VALUE')
		#	return
		if(color[0] < 0 or color[0] > 255 or color[1] < 0 or color[1] > 255 or color[2] < 0 or color[2] > 255):
			print('NOT VALID COLOR')
			return

		this.pixels[index] = color

	def fill(this, color):
		#if(len(color) == 4):
		#	print('NO ALPHA VALUE')
		if(color[0] < 0 or color[0] > 255 or color[1] < 0 or color[1] > 255 or color[2] < 0 or color[2] > 255):
			print('NOT VALID COLOR')
			return

		this.pixels = [color]*this.length

	def show(this):
		for i in range(this.length):
			this.canvas.itemconfig(this.pixelRects[i], fill = rgb_to_hex(this.pixels[i]))
		this.window.update()


theLights = Lights(FakePixels(LENGTH))

theLights.begin()