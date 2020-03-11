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

        self.bird_list = []
        self.wall_list = []
        self.player = None

        self.setup()

    def add_tuyau(self, pos):
        tuyau = arcade.Sprite("../image/pipe.png", 0.3)
        tuyau.center_x = pos
        self.wall_list.append(tuyau)

    def setup(self):
        self.background = arcade.load_texture("../image/background.png")
        self.player = arcade.Sprite("../image/bird.png", 0.25)
        self.add_tuyau(300)
        self.add_tuyau(600)
        self.add_tuyau(900)
        self.add_tuyau(1200)

        self.player.center_x = 100

    def on_draw(self ):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        for pipe in self.wall_list:
            pipe.draw()
        self.player.draw()

    def on_update(self, delta_time):
        for pipe in self.wall_list:
            hit_list =arcade.check_for_collision(self.player, pipe)
            if hit_list == True:
                self.exit_game()

            if pipe.center_x <= 0:
                pipe.center_x = 1000
            pipe.center_x -= 2
            pipe.center_y=200

        if self.player.center_y >0 :
            self.player.center_y -=  2

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            self.flap(flap=True)
            if self.player.center_y < SCREEN_HEIGHT - 40:
                self.player.center_y +=80

    def on_key_release(self, symbol: int, modifiers: int):
            self.flap(flap=False)


    def flap(self, flap):
        x = self.player.center_x
        y = self.player.center_y
        if flap:
            self.player = arcade.Sprite("../image/bird2.png", 0.25)
        else:
            self.player = arcade.Sprite("../image/bird.png", 0.25)
        self.player.center_x = x
        self.player.center_y = y


    def exit_game(self):
        exit(0)



def main():
    World(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()