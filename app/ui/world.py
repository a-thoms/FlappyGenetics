import arcade
import random

SCREEN_WIDTH = 600 * 2
SCREEN_HEIGHT = 600
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class Bird(arcade.Sprite):
    def __init__(self, id, world):
        super().__init__("../image/bird.png", 0.25)
        self.id = id
        self.world = world

        self.center_x = world.width / 8
        self.center_y = world.height / 2
        
    def draw(self):
        super().draw()
        self.center_y -= 2

    def flap(self, flap):
        if flap:
            #self.set_texture(arcade.Texture("../image/bird2.png", self.center_x, self.center_y, self.width, self.height))

            if self.center_y < self.world.height - 40:
                self.center_y += 80
        else:
            pass
            #self.set_texture(arcade.Texture("../image/bird.png", self.center_x, self.center_y, self.width, self.height))



class World(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.bird_list = []
        self.wall_list = []

        self.setup()

    def die(self, bird):
        self.bird_list.remove(bird)

    def add_tuyau(self, pos):
        tuyau = arcade.Sprite("../image/pipe.png", 0.3)
        tuyau.center_x = pos
        self.wall_list.append(tuyau)

    def setup(self):
        self.background = arcade.load_texture("../image/background.png")
        self.bird_list.append(Bird("Léo", self))
        #self.add_tuyau(300)
        self.add_tuyau(600)
        self.add_tuyau(900)
        self.add_tuyau(1200)



    def on_draw(self ):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        for pipe in self.wall_list:
            pipe.draw()
        for bird in self.bird_list:
            bird.draw()

    def on_update(self, delta_time):
        for pipe in self.wall_list:
            for bird in self.bird_list:
                hit_list = arcade.check_for_collision(bird, pipe)
                if hit_list == True:
                  self.die(bird)

            if pipe.center_x <= 0:
                pipe.center_x = 1000
            pipe.center_x -= 2
            pipe.center_y = 200
        print("update")


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            bird = self.bird_list[0]
            bird.flap(True)

    def on_key_release(self, symbol: int, modifiers: int):
        bird = self.bird_list[0]
        bird.flap(False)

    def exit_game(self):
        exit(0)



def main():
    World(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()