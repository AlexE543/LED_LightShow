import board
import neopixel
import time

class Strand():

    def __init__(self):
        self.strand = []
        for i in range(144):
            self.strand.append('')

    def add_led(self, indx, light):
        self.strand[indx] = light


class Light():
    def __init__(self, life, color):
         self.life = life
         self.color = color

    def update_life(self, life):
        self.life = life

    def decrease_life(self):
        self.life -= 1

    def change_color(self, color):
        self.color = color


def pattern1(life, color, strand, pixels):
    for i in range(144):
        try:
            strand.add_led(i, Light(life, color))
        except:
            pass
        render(strand, pixels)


def render(strand, pixels):
    for pixel in range(144):
        light = strand.strand[pixel]
        if light != '':
            light.decrease_life()
            if light.life < 0:
                light.color = (0, 0, 0)
            pixels[pixel] = light.color


if __name__ == "__main__":
    pixels = neopixel.NeoPixel(board.D18, 144, auto_write=False)
    strand = Strand()
    life = 5
    color = (138, 23, 23)
    pattern1(life, color, strand, pixels)

