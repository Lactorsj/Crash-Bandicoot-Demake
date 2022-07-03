from pygame.rect import Rect

from Crates import *


class Akuaku(Entity):
    def __init__(self, name, life_points, xPos, yPos):
        Entity.__init__(self)
        self.name = name
        self.image = pygame.image.load("assets/images/imagesPlateforme/iconeAku3.png")
        self.image = pygame.transform.scale(self.image, (14 * 3, 14 * 3))

        self.xvel = 0
        self.yvel = 0

        self.rect = Rect(xPos, yPos, 16 * 4, 32 * 4)

        self.life_points = life_points
        self.onGround = False
        self.faceright = True
        self.airborne = True
        self.attacking = False
        self.counter = 0
        self.attackcounter = 0

    def updateImg(self):
        if self.life_points == 1:
            self.image = pygame.image.load("assets/images/imagesPlateforme/iconeAku3.png")
            self.image = pygame.transform.scale(self.image, (14 * 3, 14 * 3))
        elif self.life_points == 2:
            self.image = pygame.image.load("assets/images/imagesPlateforme/iconeAku2.png")
            self.image = pygame.transform.scale(self.image, (14 * 3, 14 * 3))
        elif self.life_points >= 3:
            self.life_points = 3
            self.image = pygame.image.load("assets/images/imagesPlateforme/iconeAku1.png")
            self.image = pygame.transform.scale(self.image, (14 * 3, 14 * 3))
        elif self.life_points == 0:
            self.image = pygame.image.load("assets/images/imagesPlateforme/iconeAku0.png")
            self.image = pygame.transform.scale(self.image, (14 * 3, 14 * 3))

    def update(self, crashX, crashY):
        if self.rect.x <= crashX - 20:
            self.rect.x = crashX - 20
        if self.rect.x >= crashX + 70:
            self.rect.x = crashX + 70
        if self.rect.y <= crashY - 35:
            self.rect.y = crashY - 35
        if self.rect.y >= crashY - 20:
            self.rect.y = crashY - 20

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def _getname(self):
        return self.name

    def _getlife(self):
        if self.life_points < 0:
            self.life_points = 0
            return self.life_points
        else:
            return self.life_points

    def _setlife(self, life):
        if life < 0 and self.life_points >= life:
            self.life -= life
        else:
            self.life_points += life

    names = property(_getname)
    life = property(_getlife, _setlife)


pygame.quit()
