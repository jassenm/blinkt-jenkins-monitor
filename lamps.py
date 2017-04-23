class Lamps():

    def count_lights(self):
        return 0

    def set_light(self, index, color):
        return

    def turn_on(self):
        return

    def turn_off(self):
        return


class ConsoleLamps(Lamps):

    def __init__(self, num_lights=8):
        self.num_lights = num_lights

    def count_lights(self):
        return self.num_lights

    def set_light(self, index, color):
        print("console lamp " + str(index) + ": " + str(color))


class BlinktLamps(Lamps):

    def __init__(self):
        from blinkt import set_clear_on_exit
        set_clear_on_exit()

    def count_lights(self):
        return 8

    def turn_on(self):
        from blinkt import set_brightness
        set_brightness(1)

    def turn_off(self):
        from blinkt import set_brightness
        set_brightness(0)

    def set_light(self, index, color):
        #print("blinkt lamp " + str(index) + ": " + str(color))
        from blinkt import set_pixel, show
        set_pixel(index, color[0], color[1], color[2])
        show()
