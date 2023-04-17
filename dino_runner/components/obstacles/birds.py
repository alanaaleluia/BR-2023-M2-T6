import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Birds(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(200, 300) 


    def update(self,game_speed, obstacles):
        self.rect.x -= game_speed

        #if self.rect.x < -self.rect.width:
            #obstacles.pop()

        if self.type >= 10:
            self.type = 0

        super().update(game_speed, obstacles)

    def draw(self, screen):
        screen.blit(self.image[self.type//5], (self.rect.x, self.rect.y))
        self.type += 1