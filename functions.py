import board
import neopixel
import time

strip = neopixel.NeoPixel(board.D18, 144)

def set_all(strip, color):
    strip.fill(color)
    print("Set All")

def wipe(strip, color):
    for i in range(144):
        strip[i] = color
    print("Wiped")

def converge(strip, color):
    for i in range(72):
        strip[i], strip[143-i] = color, color
    print("Converged")

def fade(strip, color):
    for i in range(12):
        new_color = (color[0]/i, color[1]/i, color[2]/i)
        strip.fill(new_color)
    print("Faded")

set_all(strip, (144, 144, 144))
time.sleep(2)

wipe(strip, (22, 192, 34))
time.sleep(2)

converge(strip, (99, 1, 244))
time.sleep(4)

fade(strip, (255, 0, 0))
time.sleep(4)
print("Done")