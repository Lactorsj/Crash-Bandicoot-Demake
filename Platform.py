from pygame.rect import Rect

from Entity import *


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("assets/images/imagesPlateforme/grassDirtBlock.png").convert()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.flag = 1

    def update(self):
        pass
