import pygame as pg
from math import floor
from random import randint

class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        playerWalk1 = pg.image.load('img/player/sus1.png').convert_alpha()
        playerWalk2 = pg.image.load('img/player/sus2.png').convert_alpha()
        playerWalk3 = pg.image.load('img/player/sus3.png').convert_alpha()
        playerWalk4 = pg.image.load('img/player/sus4.png').convert_alpha()
        playerWalk5 = pg.image.load('img/player/sus5.png').convert_alpha()
        playerWalk6 = pg.image.load('img/player/sus6.png').convert_alpha()
        playerWalk7 = pg.image.load('img/player/sus7.png').convert_alpha()
        playerWalk8 = pg.image.load('img/player/sus8.png').convert_alpha()
        self.playerWalk =[playerWalk1, playerWalk2, playerWalk3, playerWalk4, playerWalk5, playerWalk6, playerWalk7, playerWalk8]
        self.playerIndex = 0

        self.image = self.playerWalk[self.playerIndex]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jumpSound = pg.mixer.Sound('audio/jump.mp3')
        self.jumpSound.set_volume(0.25)


    def playerInput(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.rect.bottom >= 300:
            self.jumpSound.play()
            self.gravity = -23


    def applyGravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300


    def update(self):
        self.playerInput()
        self.applyGravity()
        self.animation()

    def animation(self):
        self.playerIndex += 0.27
        self.playerIndex %= len(self.playerWalk)
        self.image = self.playerWalk[floor(self.playerIndex)]