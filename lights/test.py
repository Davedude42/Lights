import board
import neopixel

pixel_pin = board.D21
ORDER = neopixel.RGB

LENGTH = 30*5*3-18

pixels = neopixel.NeoPixel(
	pixel_pin, LENGTH, brightness=0.25, auto_write=False, pixel_order=ORDER
)
pixels.fill((0, 255, 0))
pixels.show()