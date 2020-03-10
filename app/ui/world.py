import arcade
import random

SCREEN_WIDTH = 600 *2
SCREEN_HEIGHT = 600
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class World(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("../image/background.png")


        self.bird_list = None
        self.wall_list = None
        self.player = None

        self.player = arcade.Sprite("../image/bird.png", 0.25)

        self.tuyau = arcade.Sprite("../image/pipe.png", 0.3)

        self.player.center_x = 150

        self.center_x = 1000

    def setup(self):
        pass

    def on_draw(self  ):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.center_x -= 2
        if self.center_x <= 0:
            self.center_x = 1000
        self.tuyau.center_x = self.center_x
        self.tuyau.center_y=200

        if self.player.center_y >0 :
            self.player.center_y -=  2
        self.tuyau.draw()
        self.player.draw()

    def on_update(self, delta_time):
        hit_list =arcade.check_for_collision(self.player, self.tuyau)

        print(hit_list)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            if self.player.center_y < SCREEN_HEIGHT - 40:

                self.player.center_y +=80




def main():
    World(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()