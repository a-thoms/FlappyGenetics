import arcade
import random

SCREEN_WIDTH = 600 *2
SCREEN_HEIGHT = 600

class World(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("../image/background.png")

        self.center_x =1000


    def on_draw(self):
        scale = self.width / self.background.width
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.tuyau = arcade.Sprite("../image/pipe.png", 0.3)

        self.center_x -= 2
        if self.center_x == 0:
            self.center_x = 1000
        self.tuyau.center_x = self.center_x
        self.tuyau.center_y=200
        self.tuyau.draw()

class pipeHandler(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tuyau = arcade.Sprite("../image/pipe.png", 0.3)


World(SCREEN_WIDTH,SCREEN_HEIGHT)
arcade.run()

