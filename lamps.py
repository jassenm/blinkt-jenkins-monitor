class Lamps():

    def count_lights(self):
        return 0

    def set_light(self, index, color):
        return


class ConsoleLamps(Lamps):

    def __init__(self, num_lights=8):
        self.num_lights = num_lights

    def count_lights(self):
        return self.num_lights

    def set_light(self, index, color):
        print("lamp " + str(index) +
              ": " + str(color))


class BlinktLamps(Lamps):

    def __init__(self):
        from blinkt import set_clear_on_exit
        set_clear_on_exit()

    def count_lights(self):
        return 8

    def set_light(self, index, color):
        from blinkt import set_clear_on_exit, set_pixel, show
        set_pixel(index, color[0], color[1], color[2])
