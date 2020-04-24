import arcade
import random
from app.nn.brain import Brain

BIRD = ["../image/whiteBird.png", "../image/redBird.png", "../image/purpleBird.png", "../image/blueBird.png",
        "../image/blackBird.png", "../image/yellowBird.png",  "../image/sentientBird.png",  "../image/harlequiBird.png",
        "../image/greenBird.png",  "../image/iceBird.png",  "../image/negativeBird.png", "../image/rageBird.png",
        "../image/pinkBird.png", "../image/macBird.png"]

class Bird(arcade.Sprite):
    ID = 0
    def __init__(self, world, **kwargs):
        super().__init__(BIRD[random.randint(0,len(BIRD))], 0.25)
        self.id = self.generate_id()
        self.world = world
        self.coef = 0
        self.center_x = world.width / 8
        self.center_y = world.height / 2
        self.distance = 0

        if kwargs["brain"]:
            self.brain = kwargs["brain"]
        else:
            self.brain = Brain(2, 32, 1)

    def generate_id(self):
        Bird.ID += 1
        return Bird.ID

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

    def crossover(self, bird):
        brain1, brain2 = self.brain.crossover(bird.brain)
        return Bird(self.world, brain=brain1), Bird(self.world, brain=brain2)

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


