import pygame as pg
from math import floor
from random import randint

class Enemy(pg.sprite.Sprite):

	def __init__(self, enemyType):
		super().__init__()
		
		if enemyType == 0:
			enemy1Frame1 = pg.image.load("img/Snail/snail1.png").convert_alpha()
			self.frames = [enemy1Frame1]
			yPos = 300

		else:
			enemy2Frame1 = pg.image.load("img/Fly/Fly1.png").convert_alpha()
			enemy2Frame2 = pg.image.load("img/Fly/Fly2.png").convert_alpha()
			self.frames = [enemy2Frame1, enemy2Frame2]
			yPos = 210

		self.frameIndex = 0

		self.image = self.frames[self.frameIndex]
		self.rect = self.image.get_rect(midbottom = (randint(900, 1100), yPos))


	def animation(self):
		self.frameIndex += 0.1
		self.frameIndex %= len(self.frames)
		self.image = self.frames[floor(self.frameIndex)]


	def update(self):
		self.animation()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100:
			self.kill()