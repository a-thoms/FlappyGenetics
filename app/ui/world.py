import arcade
import random

SCREEN_WIDTH = 600 *2
SCREEN_HEIGHT = 600

class World(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("../image/background.png")

    def on_draw(self):
        scale = self.width / self.background.width
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

World(SCREEN_WIDTH,SCREEN_HEIGHT)
arcade.run()