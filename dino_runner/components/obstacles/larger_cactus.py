import random

from dino_runner.components.obstacles.obstacle import Obstacle

POS_Y = 290

class LargerCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = POS_Y