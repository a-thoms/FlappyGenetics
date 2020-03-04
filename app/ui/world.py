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
        tuyau = arcade.Sprite("../image/pipe.png", 0.5)
        self.center_x -=1
        tuyau.center_x = self.center_x
        tuyau.center_y=300
        tuyau.draw()



World(SCREEN_WIDTH,SCREEN_HEIGHT)
arcade.run()

