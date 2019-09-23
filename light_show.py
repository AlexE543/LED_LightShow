import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 144, auto_write=False)

def alternating(color_1, color_2):
    while True:
        time.sleep(.5)
        for i in range(72):
            pixels[i*2] = color_1
            pixels[i*2 +1] = color_2
        pixels.show()
        time.sleep(.5)
        for j in range(72):
            pixels[j*2] = color_2
            pixels[j*2 +1] = color_1
        pixels.show()

col_1 = (255, 0, 0)
col_2 = (0, 0, 255)
alternating(col_1, col_2)

