import board
import neopixel

strip = neopixel.NeoPixel(board.D18, 144, brightness=0.2, auto_write=False)
# Sets all the leds to the same color
def set_all(strip, color):
    strip.fill(color)
    strip.show()

# Wipes a color down the strand to fill it with that color
def wipe(strip, color):
    for i in range(144):
        strip[i] = color
        strip.show()
    print("Wiped")

# Starts at both ends of the strand and fills the strand with the color
def converge(strip, color):
    for i in range(72):
        strip[i], strip[143-i] = color, color
        strip.show()
    print("Converged")

# Fades the strip from one color to dark
def fade(strip, color):
    for i in range(1, 12):
        step_size = 255//12
        new_color = (color[0]-(i*step_size), color[1]-(i*step_size), color[2]-(i*step_size))
        strip.fill(new_color)
        strip.show()
    new_color = ((0, 0, 0))
    strip.fill(new_color)
    strip.show()

def shoot(strip, color):
    for i in range(0, 144, 2):
        if i >= 8:
            strip[i] = color
            strip[i - 2] = tuple(map(lambda x: x//2, color))
            strip[i - 4] = tuple(map(lambda x: x//4, color))
            strip[i - 6] = (0, 0, 0)
            strip.show()

# print("Shoot")
# for i in range(200):
#     shoot(strip, (255, 255, 0))
# set_all(strip, (144, 144, 144))
# time.sleep(2)
#
# wipe(strip, (22, 192, 34))
# time.sleep(2)
#
# converge(strip, (99, 1, 244))
# time.sleep(4)
#
# fade(strip, (255, 0, 0))
# time.sleep(4)
# print("Done")