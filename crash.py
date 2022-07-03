from SpriteSheet import *
from akuaku import *
from enemy import *


class Crash(Entity):
    def __init__(self, name, x, y, life_points, damage=1, attack=0):
        Entity.__init__(self)

        self.name = name
        self.life_points = life_points
        self.damage = damage
        self.attack = attack
        self.rect = Rect(x, y, 16 * 3, 32 * 3)
        self.wumpafruit = 0

        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.airborne = True
        self.attacking = False
        self.counter = 0
        self.attackcounter = 0
        self.player_img = "Assets/images/personnages/crashspritesheet.png"
        self.all_frames = self.load_frames_from_sheet()
        self.image = self.all_frames.get("right").get("stand")[0]
        self.vel_y = 0
        self.current_frame = 0
        self.jumped = False
        self.direction = 1
        self.dir_frames = []
        self.frames = []
        self.state = "walk"
        self.x_move = 0
        self.y_move = 0
        self.is_attack = False
        self.last_updated = 0
        self.current_image = self.all_frames.get(
            "left").get("stand")[0].get_rect()
        self.transition_timer = 0
        self.hurt_invisible_timer = 0

        self.aku = Akuaku("Aku", 2, self.rect.x - 30, self.rect.y - 130)

    def _getname(self):
        return self.name

    def _getxposition(self):
        return self.rect.x

    def _setxposition(self, position):
        self.rect.x = position

    def _getyposition(self):
        return self.rect.y

    def _setyposition(self, position):
        self.rect.y = position

    def _getlife(self):
        if self.life_points < 0:
            self.life_points = 0
            return self.life_points
        else:
            return self.life_points

    def _setlife(self, life):
        if life < 0 and self.life_points >= abs(life):
            self.life_points += life
        else:
            self.life_points += life

    def _getdamage(self):
        if self.damage < 0:
            return self.damage == 0
        else:
            return self.damage

    def _setdamage(self, takedamage):
        if takedamage > 0 and self.life_points >= takedamage:
            self.life_points -= takedamage
        elif takedamage > 0 and self.life_points > 0 and self.life_points < takedamage:
            self.life_points = 0
        else:
            self.life_points = self.life_points

    def _getattack(self):
        if self.attack > 0:
            return str("{} a recu {} attaques ".format(self.names, self.attack))
        else:
            return str("{} n'a pas recu d'attaques ".format(self.names))

    def _setattack(self, addattack):
        if addattack > 0:
            self.attack += addattack
        else:
            self.attack += 0

    def attack_target(self, target_player):
        target_player._setdamage(self.damage)
        target_player.attack += 1

    def _getwumpafruit(self):
        return self.wumpafruit

    def _setwumpafruit(self, nb):
        if nb < 1:
            self.wumpafruit += 0
        else:
            self.wumpafruit += nb

    def soundbox(self, chemin):
        self.boxsound = pygame.mixer.Sound(chemin)
        self.boxsound.play(loops=0, maxtime=1500)
        self.boxsound.set_volume(0.3)

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
        my_sprite_sheet = SpriteSheet(self.player_img)
        stand_frames = [my_sprite_sheet.parse_sprite("stand")]
        move_frames = [my_sprite_sheet.parse_sprite(
            "walk{}".format(i)) for i in range(0, 7)]
        jump_frames = [my_sprite_sheet.parse_sprite(
            "jump{}".format(i)) for i in range(0, 3)]
        revolve_frames = [my_sprite_sheet.parse_sprite(
            "revolve{}".format(i)) for i in range(0, 11)]
        right_frames = {"stand": stand_frames,
                        "walk": move_frames,
                        "jump": jump_frames,
                        "revolve": revolve_frames}
        left_frames = {key: [pygame.transform.flip(frame, True, False) for frame in frames]
                       for key, frames in right_frames.items()}
        all_frames = {"left": left_frames, "right": right_frames}
        return all_frames

    def update(self, up, down, left, right, attack, platforms, enemygroup):
        self.state = "stand"
        if up:
            if self.onGround:
                self.yvel -= 19
                self.state = "jump"

        if down:
            if self.onGround:
                self.yvel += 19
        if attack:
            self.attack = False
            self.attacking = True
            self.state = "revolve"
        if left:
            self.xvel = -8
            self.direction = -1
            self.state = "walk"
        if right:
            self.xvel = 8
            self.direction = 1
            self.state = "walk"

        if not self.onGround:
            self.yvel += 1.4

        if not (left or right):
            self.xvel = 0
        if self.yvel < 0 or self.yvel > 1.2:
            self.airborne = True
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, enemygroup)
        self.rect.top += self.yvel
        self.onGround = False
        self.collide(0, self.yvel, platforms, enemygroup)
        self.handle_state()
        self.animate()

        if self.attackcounter > 8:
            self.attacking = False
            self.attackcounter = 0
            self.counter = 0
            print("OK")

        return up or down or left or right or attack or platforms

    def collide(self, xvel, yvel, platforms, enemygroup):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if isinstance(p, CrashBox):
                    self.life_points += p.lifeplus
                    p.lifeplus -= p.lifeplus
                    p.kill()
                    if p.flag == 1:
                        self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                        p.flag = 0
                    continue
                if isinstance(p, WumpaBigBox):
                    self.wumpafruit += p.wumpafruitplus
                    p.wumpafruitplus -= p.wumpafruitplus
                    if p.flag == 1:
                        self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                        p.flag = 0
                    p.kill()
                    continue

                if isinstance(p, AkuBox):
                    print("This A")
                    self.aku.life_points += p.lifePointAku
                    p.lifePointAku -= p.lifePointAku
                    if p.flag == 1:
                        self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                        p.flag = 0
                    p.kill()
                    continue

                if isinstance(p, NitroBox):
                    if (self.state == "revolve"):
                        if self.aku.life_points <= 3 and self.aku.life_points > 0:
                            self.aku.life_points -= 1
                        else:
                            self.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/bombeNitro.ogg")
                            p.flag = 0
                        p.kill()
                    else:
                        pass
                    continue

                if isinstance(p, TntBox):
                    if (self.state == "revolve"):
                        if self.aku.life_points <= 3 and self.aku.life_points > 0:
                            self.aku.life_points -= 1
                        else:
                            self.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/bombeNitro.ogg")
                            p.flag = 0
                        p.kill()
                    else:
                        pass
                    continue

                if isinstance(p, ArrowBox):
                    print("Interact with Arrow")
                    self.yvel = -22
                    continue

                if isinstance(p, Wumpa):
                    self.wumpafruit += p.wumpafruitplus
                    p.wumpafruitplus -= p.wumpafruitplus
                    if p.flag == 1:
                        self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                        p.flag = 0
                    p.kill()
                    continue

                if isinstance(p, WumpaSmallBox):
                    self.wumpafruit += p.wumpafruitplus
                    p.wumpafruitplus -= p.wumpafruitplus
                    if p.flag == 1:
                        self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                        p.flag = 0
                    p.kill()
                    continue

                if isinstance(p, Obstacle):

                    if self.aku.life_points <= 3 and self.aku.life_points > 0:
                        self.aku.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/sonFall.ogg")
                            p.flag = 0
                        continue
                    else:
                        self.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/sonAttak.ogg")
                            p.flag = 0
                        self.rect.x = 100
                        self.rect.y = 100
                        continue

                if isinstance(p, ObstacleWater):

                    if self.aku.life_points <= 3 and self.aku.life_points > 0:
                        self.aku.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/son1.ogg")
                            p.flag = 0
                        continue
                    else:
                        self.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/sonFall.ogg")
                            p.flag = 0
                        self.rect.x = 100
                        self.rect.y = 100
                        continue

                if isinstance(p, ObstacleSpikePillar):
                    if self.aku.life_points <= 3 and self.aku.life_points > 0:
                        self.aku.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/sonAttak.ogg")
                            p.flag = 0
                        continue
                    else:
                        self.life_points -= 1
                        if p.flag == 1:
                            self.soundbox("assets/sons/son1.ogg")
                            p.flag = 0
                        self.rect.x = 100
                        self.rect.y = 100
                        continue

                if xvel > 0:
                    self.rect.right = p.rect.left
                    print("collide right")
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print("collide left")
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

                for e in enemygroup:
                    if pygame.sprite.collide_rect(self, e):
                        if isinstance(e, crabe):
                            if (self.state == "revolve"):
                                e.kill()
                            else:
                                if self.aku.life_points <= 3 and self.aku.life_points > 0:
                                    self.aku.life_points -= 1
                                    self.soundbox("assets/sons/sonAttak.ogg")

                                else:
                                    self.life_points -= 1
                                    self.soundbox("assets/sons/sonAttak.ogg")

                            continue
                        if isinstance(e, skunk):
                            if (self.rect.bottom == e.rect.top or self.state == "revolve"):
                                e.kill()
                            else:
                                pass
                            continue

                        if isinstance(e, Piranha):
                            if self.aku.life_points <= 3 and self.aku.life_points > 0:
                                self.aku.life_points -= 1
                                self.soundbox("assets/sons/sonAttak.ogg")

                            else:
                                self.life_points -= 1
                                self.soundbox("assets/sons/sonAttak.ogg")
                            continue

                        if isinstance(e, Fire):
                            if self.aku.life_points <= 3 and self.aku.life_points > 0:
                                self.aku.life_points -= 1
                                self.soundbox("assets/sons/sonAttak.ogg")

                            else:
                                self.life_points -= 1
                                self.soundbox("assets/sons/sonAttak.ogg")

                            continue

    names = property(_getname)
    life = property(_getlife, _setlife)
    damages = property(_getdamage, _setdamage)
    attacks = property(_getattack, _setattack)
    wumpafruits = property(_getwumpafruit, _setwumpafruit)
    Xpos = property(_getxposition, _setxposition)
    Ypos = property(_getyposition, _setyposition)
