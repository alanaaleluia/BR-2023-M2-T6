import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.larger_cactus import LargerCactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

        
    def update(self, game):
        if len(self.obstacles) == 0:
            randomSpawn = random.randint(0, 2)
            if randomSpawn == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            if randomSpawn == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            if randomSpawn == 2:
                self.obstacles.append(Birds(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
        
        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)