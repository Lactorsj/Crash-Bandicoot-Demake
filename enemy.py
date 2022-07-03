from pygame import Surface
from pygame.rect import Rect

from Crates import *
from SpriteSheet_flower import *

spritesheet = pygame.image.load("assets/images/ennemies/crab.png")
spritesheet1 = pygame.image.load("assets/images/ennemies/skunk.png")

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet1,(0,0))
character = pygame.transform.scale(character, (16*3,16*3))
skunk1 = character

character = Surface((48,48),pygame.SRCALPHA)
character.blit(spritesheet,(0,0))
character = pygame.transform.scale(character, (48,48))
crab = character

class crabe(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.xvel = 1
        self.yvel = 0
        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.image = crab
        self.rect = Rect(x, y , 16*3 , 16*3)
        self.flag = 1

    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 100: self.yvel = 100

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.onGround = False
        self.collide(0, self.yvel, platforms, entities)
        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0

    def animate(self):

        if not self.destroyed: self.walkloop()
        else: self.destroyloop()

    def walkloop(self):
        if self.counter == 10:
            self.updatecharacter(crab)
        elif self.counter == 20:
            self.updatecharacter(crab)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        if self.counter == 0:
            self.updatecharacter(crab)
        elif self.counter == 10: self.kill()
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        self.image = ansurf

class skunk(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.xvel = 1
        self.yvel = 0
        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.image = skunk1
        self.rect = Rect(x, y , 16*3 , 16*3)
        self.flag = 1


    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 100: self.yvel = 100

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, entities)
        self.rect.top += self.yvel
        self.onGround = False
        self.collide(0, self.yvel, platforms, entities)

        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0

    def animate(self):
        if not self.destroyed: self.walkloop()
        else: self.destroyloop()

    def walkloop(self):
        if self.counter == 10:
            self.updatecharacter(skunk1)
        elif self.counter == 20:
            self.updatecharacter(skunk1)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        if self.counter == 0:
            self.updatecharacter(skunk1)
        elif self.counter == 10: self.kill()
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        self.image = ansurf

class Piranha(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.filename = "Assets/images/ennemies/flower.png"
        self.destroyed = False
        self.counter = 0
        self.rect = Rect(x, y , 16*3 , 16*3)
        self.frames = []
        self.all_frames = self.load_frames_from_sheet()
        self.image = self.all_frames.get("left").get("move")[0]
        self.current_frame = 0
        self.current_image = self.all_frames.get("left").get("move")[0].get_rect()
        self.last_updated = 0
        self.flag = 1


    def animate(self):
        now = pygame.time.get_ticks()#动画开始时间
        if now - self.last_updated > 100:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.current_image = self.frames[self.current_frame]
            self.image = self.frames[self.current_frame]

    def load_frames_from_sheet(self):
        my_sprite_sheet = SpriteSheetFlower(self.filename)
        move_frames = [my_sprite_sheet.parse_sprite(
            "flower{}".format(i)) for i in range(0, 17)]
        right_frames = {"move": move_frames}
        left_frames = {key: [pygame.transform.flip(frame, True, False) for frame in frames]
            for key, frames in right_frames.items()}
        all_frames = {"left": left_frames}
        self.frames = all_frames.get("left").get("move")
        return all_frames

    def update(self,platforms, entities):
            self.animate()