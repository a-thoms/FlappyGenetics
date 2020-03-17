import arcade
import random

SCREEN_WIDTH = 600 * 2
SCREEN_HEIGHT = 600
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

PX_BETWEEN_PIPE = SCREEN_WIDTH / 3

BIRD = ["../image/whiteBird.png", "../image/redBird.png", "../image/purpleBird.png", "../image/blueBird.png",
        "../image/blackBird.png", "../image/yellowBird.png",  "../image/sentientBird.png",  "../image/harlequiBird.png",
        "../image/greenBird.png",  "../image/iceBird.png",  "../image/negativeBird.png", "../image/rageBird.png",
        "../image/pinkBird.png", "../image/macBird.png"]

class Bird(arcade.Sprite):
    def __init__(self, id, world):
        super().__init__(BIRD[random.randint(0,len(BIRD))], 0.25)
        self.id = id
        self.world = world
        self.coef = 0
        self.center_x = world.width / 8
        self.center_y = world.height / 2

    def draw(self):
        super().draw()
        self.coef += 1
        move = 1.4*self.coef - 0.11 * (self.coef**2)
        if move <= -4.5:
            move = -4.5

        elif move > 32:
            move = 32
        self.turn_left(move/6)
        self.center_y = self.center_y + move

    def flap(self, flap):
        if flap:
            if self.center_y <= self.world.height - (self.height/2) -10:
                self.coef = 0
            #self.set_texture(arcade.Texture("../image/bird2.png", self.center_x, self.center_y, self.width, self.height))

            #if self.center_y <= self.world.height - 40:
             # self.center_y += 60
        else:
            pass
            #self.set_texture(arcade.Texture("../image/bird.png", self.center_x, self.center_y, self.width, self.height))



class World(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.bird_list = []
        self.wall_list = arcade.SpriteList()

        self.setup()

        self.loopCount = 0

    def die(self, bird):
        self.bird_list.remove(bird)

    def add_tuyau(self, posX, posY):
        tuyau = arcade.Sprite("../image/pipeUp.png", 0.35)
        tuyauDown = arcade.Sprite("../image/pipeDown.png", 0.35)

        tuyau.center_x = posX
        tuyau.center_y = posY

        tuyauDown.center_x = posX
        tuyauDown.center_y = posY + self.height +  20

        self.wall_list.append(tuyau)
        self.wall_list.append(tuyauDown)

    def setup(self):
        self.background = arcade.load_texture("../image/background.png")
        self.bird_list.append(Bird("Léo", self))

        self.add_tuyau(self.width/2, 200)
        self.add_tuyau((self.width/2) + PX_BETWEEN_PIPE, random.randint(-120, 230))
        self.add_tuyau((self.width/2) + PX_BETWEEN_PIPE*2, random.randint(-120, 230))




    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.wall_list.draw()
        for bird in self.bird_list:
            bird.draw()

    def on_update(self, delta_time):
        pipeToRemove = []
        for pipe in self.wall_list:
            pipe.center_x -= 3
            for bird in self.bird_list:
                hit_list = arcade.check_for_collision(bird, pipe)
                if hit_list or bird.center_y <= 12 :
                    self.die(bird)

            if pipe.center_x + pipe.width/2 <= 0:
                pipeToRemove.append(pipe)

        for pipe in pipeToRemove:
            pipe.remove_from_sprite_lists()
            if len(self.wall_list) % 2 == 0:
                self.add_tuyau(self.width, random.randint(-130, 230))



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            bird = self.bird_list[0]
            bird.flap(True)

        if key == arcade.key.Z:
            if len(self.bird_list) == 0:
                self.bird_list.append(Bird("Léo", self))
            else:
                pass
        if key == arcade.key.A:
            self.bird_list.append(Bird("Léo", self))

    def on_key_release(self, symbol: int, modifiers: int):
        bird = self.bird_list[0]
        bird.flap(False)

    def exit_game(self):
        exit(0)



def main():
    world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
    print("Final :", len(world.wall_list))

if __name__ == "__main__":
    main()