import pygame
from PIL import ImageTk
from pygame import *
import time, sys, os

import tkinter
from tkinter import *
from tkinter import ttk
from crash import Crash
from akuaku import Akuaku

from Entity import *
from Camera import *
from Platform import *
from Crates import *
from enemy import *





def menu():
    wind = tkinter.Tk()
    wind.geometry("600x400")
    wind.resizable(0, 0)
    wind.iconphoto(False, tkinter.PhotoImage(file='Assets/images/imagesPlateforme/logo.png'))
    wind.title("Crash Bandicoot")
    menu1 = tkinter.Menu(wind)
    col1 = tkinter.Menu(menu1, tearoff=0)
    # Background
    bgImage = PhotoImage(file="assets/images/imagesPlateforme/menu2.png")
    tkinter.Label(wind, image=bgImage).place(relwidth=1, relheight=1)


    wind.config(menu=menu1, background='purple')
    button = Button(wind, text="Start Game", bg='#FFCC00', fg='#CA0000', font=('Lucida', 15, 'bold'), relief=RIDGE,
                    width=10, borderwidth=1, command=wind.quit)
    button.pack()
    button.place(x=250, y=225)
    wind.mainloop()


# from time import sleep

WIN_WIDTH = 1000
WIN_HEIGHT = 500
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

pygame.init()
music = pygame.mixer.music.load('assets/musique/crash-bandicoot-music-jungle-rollers-rolling-stones-extended-hd.mp3')
icon = pygame.image.load("Assets/images/imagesPlateforme/logo.png")
pygame.display.set_icon(icon)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


def Main():
    background = pygame.image.load(
        "assets/images/imagesPlateforme/background.png")  # Image du font d'écran(arrière plan)

    crashlife_pic = pygame.image.load('assets/images/imagesPlateforme/iconeCrash.png')
    crashlife_pic = pygame.transform.scale(crashlife_pic, (14 * 3, 14 * 3))
    crashlife_pic_x = 3
    crashlife_pic_y = 4

    wumpafruit_pic = pygame.image.load('assets/images/imagesPlateforme/iconeWumpa.png')
    wumpafruit_x = 10
    wumpafruit_y = 40

    aku_aku_pic = pygame.image.load('assets/images/imagesPlateforme/iconeAku1.png')
    aku_aku_pic_x = 10
    aku_aku_pic_y = 70

    def gameover(screen):
        myfont = pygame.font.SysFont("segoeprint", 70)
        img = pygame.image.load("assets/images/imagesPlateforme/menu3.png").convert()
        screen.blit(img, (0, 0))
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if 450 < pos[0] < 900 and \
                    120 < pos[1] < 200:
                pygame.quit()
                sys.exit()

    font_text = pygame.font.SysFont("franklingothicmedium", 30)
    menu()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    crash2 = Crash("Crashou", 16 * 3, 16 * 3 * 9, life_points=4, damage=2, attack=2)
    aku = crash2.aku
    launched = True
    while launched:
        pygame.display.set_caption("Use arrows to move!")  # Permet de titrer le fenêtre
        timer = pygame.time.Clock()
        timer.tick(60)

        up = down = left = right = attack = False

        entities = pygame.sprite.Group()

        enemygroup = pygame.sprite.Group()
        enemygroup.add(crabe(16 * 3 * 6, 16 * 3 * 9))
        enemygroup.add(crabe(16 * 3 * 10, 16 * 3 * 9))
        enemygroup.add(crabe(16 * 3 * 75, 16 * 3 * 9))

        enemygroup.add(skunk(16 * 3 * 20, 16 * 3 * 9))
        enemygroup.add(skunk(16 * 3 * 120, 16 * 3 * 9))
        enemygroup.add(skunk(16 * 3 * 90, 16 * 3 * 9))

        enemygroup.add(Piranha(16 * 3 * 25, 16 * 3 * 8))

        enemygroup.add(Fire(16 * 3 * 22, 16 * 3 * 8))

        platforms = []

        x = y = 0
        level = [

            "D                                                                                                                                                                              D",
            "D                                                                                                                                                                              D",
            "D                                        B SS                                                                                                                                  D",
            "D                         K                               T BT                                                                 FFFF                                            D",
            "D                      C  K  B      R                SPPPPPPPPPPPP                     BBBB                                                             I                      D",
            "D       B  AA    A    PPPPPPP                     PP                         B                                B        B   E       SES           R      I                      D",
            "D                   PP                             FFF                                                                 PPPPPPPPPPPP                     I                      D",
            "D           S  S                 FFFFF        II                       FFF                                          PP           R                      I                SSS   D",
            "D          N     T     N        I     I       II       I    I      B  N    C         A R      I  SS     I    NR                T      K B K FFFF  I     I                BBB   D",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPPPPPPPP    PPPPPPPPPPPPPWWWWWPPPPWWWWPPPPPPPPP     PPPPPPPPIIIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPWWWWPPPPPPPPP",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDHHHHHDDDDDDDDDDDDDDDDDDHHHHDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDHHHHHDDDDDDDD   DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDHHHHHDDDDDDDDDDDDDDDDDDDDDDDD",
        ]

        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = CrashBox(x, y)
                    platforms.append(e)
                    entities.add(e)

                if col == "D":
                    e = DirtBlock(x, y)
                    platforms.append(e)
                    entities.add(e)

                if col == "B":
                    b = WumpaBigBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "I":
                    b = IronBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "N":
                    b = NitroBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "T":
                    b = TntBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "R":
                    b = ArrowBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "F":
                    b = Wumpa(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "A":
                    b = AkuBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "S":
                    b = WumpaSmallBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "H":
                    b = Obstacle(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "W":
                    b = ObstacleWater(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "K":
                    b = ObstacleSpikePillar(x, y)
                    platforms.append(b)
                    entities.add(b)

                x += 16 * 3
            y += 16 * 3
            x = 0

        total_level_width = len(level[0]) * 16 * 3
        total_level_height = len(level) * 16 * 3
        camera = Camera(complex_camera, total_level_width, total_level_height)
        entities.add(crash2)
        entities.add(aku)

        while 1:
            timer.tick(60)
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYDOWN and e.key == K_SPACE:
                    print("Attack")
                    attack = True

                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
                if e.type == KEYUP and e.key == K_SPACE:
                    attack = False

            screen.blit(background, (0, 0))

            camera.update(crash2)

            crash2.update(up, down, left, right, attack, platforms, enemygroup)
            aku.updateImg()
            aku.update(crash2.Xpos, crash2.Ypos)

            for e in entities:
                screen.blit(e.image, camera.apply(e))

            for e in enemygroup:
                screen.blit(e.image, camera.apply(e))
                e.update(platforms, entities)

            if crash2.wumpafruit >= 100:
                crash2.life_points += 1
                crash2.wumpafruit = 0

            screen.blit(crashlife_pic, (crashlife_pic_x, crashlife_pic_y))
            screen.blit(wumpafruit_pic, (wumpafruit_x, wumpafruit_y))
            screen.blit(aku_aku_pic, (aku_aku_pic_x, aku_aku_pic_y))

            points_de_vie_crash = font_text.render(": {}".format(crash2.life), True, (255, 255, 255))
            wumpa_fruits_gagnes = font_text.render(": {}".format(crash2.wumpafruit), True, (255, 255, 255))
            aku_aku_life = font_text.render(": {}".format(crash2.aku.life_points), True, (255, 255, 255))

            screen.blit(points_de_vie_crash, [40, 10])
            screen.blit(wumpa_fruits_gagnes, [40, 40])
            screen.blit(aku_aku_life, [40, 70])

            if crash2.life_points < 1:
                gameover(screen)
                pygame.mixer.music.stop()

            pygame.display.update()


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)
    return Rect(l, t, w, h)


if __name__ == '__main__':
    Main()
