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
        self.center_x =1000

        self.bird_list = None
        self.wall_list = None

        self.bird = None

    def setup(self):
        """ Setup the game at the beginning"""
        # Create the Sprite lists
        self.bird_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.bird = arcade.Sprite("../image/bird.png", 0.25)
        self.bird.center_x = 100
        self.bird.center_y = 100
        self.bird_list.append(self.bird)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite("../image/ground.png", 0.3)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.tuyau = arcade.Sprite("../image/pipe.png", 0.3)

        self.center_x -= 2
        if self.center_x <= 0:
            self.center_x = 1000
        self.tuyau.center_x = self.center_x
        self.tuyau.center_y=200
        self.tuyau.draw()
        self.bird.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.bird.change_y = PLAYER_JUMP_SPEED

class pipeHandler(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tuyau = arcade.Sprite("../image/pipe.png", 0.3)


World(SCREEN_WIDTH,SCREEN_HEIGHT)
World.setup()
arcade.run()

