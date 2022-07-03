from pygame.rect import Rect

from Platform import *
from SpriteSheet_TNT import SpriteSheetTNT
from SpriteSheet_fire import SpriteSheetFire

class WumpaSmallBox(Platform): #1
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/BasicCrate.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.wumpafruitplus = 5
        self.flag = 1

    def __del__(self):
        if self.wumpafruitplus == 0:
            print("objet detruit ! ")

class WumpaBigBox(Platform): #2
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/bigcrate.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.wumpafruitplus = 10
        self.flag = 1


    def __del__(self):
        if self.wumpafruitplus == 0:
            print("objet detruit ! ")

class ArrowBox(Platform):#3
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxFleche.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.flag = 1

    def __del__(self):
        print("objet detruit ! ")

class AkuBox(Platform):#4
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxAku.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.lifePointAku = 1
        self.flag = 1

    def __del__(self):
        if self.lifePointAku == 0:
            print("objet detruit ! ")

class CrashBox(Platform):#5
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxCrash.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.lifeplus = 1

    def __del__(self):
        if self.lifeplus == 0:
            print("objet detruit ! ")

class IronBox(Platform):#6
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxAcier.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.flag = 1

class TntBox(Platform):#7
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxTNT.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.damage = 1
        self.flag = 1

    def handle_state(self):
        """根据状态决定行为"""
        if self.direction == -1:
            self.dir_frames = self.all_frames.get("left")
        else:
            self.dir_frames = self.all_frames.get("right")

        if self.state == "walk":
            self.frames = self.dir_frames.get("walk")
        elif self.state == "stand":
            self.frames = self.dir_frames.get("stand")
        elif self.state == "jump":
            self.frames = self.dir_frames.get("jump")
        elif self.state == "revolve":
            self.frames = self.dir_frames.get("revolve")

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 100:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.current_image = self.frames[self.current_frame]
            self.image = self.frames[self.current_frame]

    def load_frames_from_sheet(self):
        my_sprite_sheet = SpriteSheetTNT(self.player_img)
        stand_frames = [my_sprite_sheet.parse_sprite("stand")]
        move_frames = [my_sprite_sheet.parse_sprite(
            "walk{}".format(i)) for i in range(0, 7)]
        jump_frames = [my_sprite_sheet.parse_sprite(
            "jump{}".format(i)) for i in range(0, 3)]
        revolve_frames = [my_sprite_sheet.parse_sprite(
            "revolve{}".format(i)) for i in range(0, 11)]
        right_frames = {"stand":stand_frames,
                        "walk": move_frames,
                        "jump":jump_frames,
                        "revolve":revolve_frames}
        left_frames = {key: [pygame.transform.flip(frame, True, False) for frame in frames]
                    for key, frames in right_frames.items()}
        all_frames = {"left": left_frames, "right": right_frames}
        return all_frames

class NitroBox(Platform):#8
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxNitro.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.damage = 1
        self.flag = 1

class DirtBlock(Platform):  #土块
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/imagesPlateforme/DirtBlock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)

class Wumpa(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/wumpa.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.wumpafruitplus = 1
        self.flag = 1

    def __del__(self):
        if self.wumpafruitplus == 0:
            print("objet detruit ! ")

class Obstacle(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x , y )
        self.image = pygame.image.load("assets/images/obstacles/hole.png")
        self.image = pygame.transform.scale(self.image, (60, 20))
        self.rect = Rect(x, y, 32, 32)
        self.damage = 1

    def __del__(self):
            print("objet detruit ! ")

class ObstacleWater(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x , y )
        self.image = pygame.image.load("assets/images/obstacles/water.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = Rect(x, y, 32, 32)

    def __del__(self):
            print("objet detruit ! ")

class ObstacleSpikePillar(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x , y )
        self.image = pygame.image.load("assets/images/obstacles/spikePillar.png")
        self.image = pygame.transform.scale(self.image, (16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

    def __del__(self):
            print("objet detruit ! ")

class Gagner(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/imagesPlateforme/exit.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16* 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)

class Fire(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.filename = "Assets/images/obstacles/fire.png"
        self.destroyed = False
        self.counter = 0
        self.rect = Rect(x, y , 16*3 , 16*3)
        self.frames = []
        self.all_frames = self.load_frames_from_sheet()
        self.image = self.all_frames.get("left").get("move")[0]
        self.current_frame = 0
        self.current_image = self.all_frames.get("left").get("move")[0].get_rect()
        self.last_updated = 0
        self.last_updated2 = 0
        self.timer = 0
        self.state = 1

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 100:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.current_image = self.frames[self.current_frame]
            self.image = self.frames[self.current_frame]

    def load_frames_from_sheet(self):
        my_sprite_sheet = SpriteSheetFire(self.filename)
        move_frames = [my_sprite_sheet.parse_sprite(
            "fire{}".format(i)) for i in range(0, 16)]
        left_frames = {"move": move_frames}
        all_frames = {"left": left_frames}
        self.frames = move_frames
        return all_frames

    def update(self,platforms, entities):
        self.animate()