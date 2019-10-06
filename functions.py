import board
import neopixel
import time

strip = neopixel.NeoPixel(board.D18, 144, brightness=0.2, auto_write=False)

def set_all(strip, color):
    strip.fill(color)
    strip.show()
    print("Set All")

def wipe(strip, color):
    for i in range(144):
        strip[i] = color
        strip.show()
    print("Wiped")

def converge(strip, color):
    for i in range(72):
        strip[i], strip[143-i] = color, color
        strip.show()
    print("Converged")

def fade(strip, color):
    for i in range(1, 12):
        new_color = (color[0]//i, color[1]//i, color[2]//i)
        strip.fill(new_color)
        strip.show()
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