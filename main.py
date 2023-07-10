from Lights import Lights

import board
import neopixel

LENGTH = 30*5*3-18

pixels = neopixel.NeoPixel(
	board.D21, LENGTH, brightness=0.25, auto_write=False, pixel_order=neopixel.GRB
)

theLights = Lights(pixels)

theLights.begin()