import pygame as pg
from sys import exit
from math import floor
from random import randint

from player import Player
from enemy import Enemy


def displayScore():
	currentTime = (pg.time.get_ticks() - startTime) // 1000
	scoreSurf = testFont.render(f"{currentTime}", False, (64,64,64))
	scoreRect = scoreSurf.get_rect(center=(400, 50))
	screen.blit(scoreSurf, scoreRect)
	return currentTime

def collisions():
	if pg.sprite.spritecollide(player.sprite, enemyGroup, False):
		enemyGroup.empty()
		player.sprite.rect.y = 300
		return False
	else:
		return True



pg.init()

width, height = 800, 400
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Endless Runner Game")
clock = pg.time.Clock()
testFont = pg.font.Font('font/templeos_font.ttf', 25)
gameActive = False
startTime = 0
score = 0

# When i make background music to add in:
#backgroundMusic = pg.mixer.Sound('audio/backgroundMusic.wav')
#backgroundMusic.set_volume(0.075)
#backgroundMusic.play(loops = -1)

skySurface = pg.image.load('img/Sky.png').convert()
groundSurface = pg.image.load('img/ground.png').convert()

# Player group:
player = pg.sprite.GroupSingle()
player.add(Player())

# Enemy group:
enemyGroup = pg.sprite.Group()

# Intro/gameover screen:
playerStand = pg.image.load('img/player/sus1.png').convert_alpha()
playerStand = pg.transform.scale2x(playerStand)
playerStandRect = playerStand.get_rect(center = (400, 200))

gameName = testFont.render("Endless Runner", False, (111, 196, 169))
gameNameRect = gameName.get_rect(center=(400, 75))

gameMessage = testFont.render("press space to run", False, (111, 196, 169))
gameMessageRect = gameMessage.get_rect(center=(400, 330))


# Timer:
obstacleTimer = pg.USEREVENT + 1
pg.time.set_timer(obstacleTimer, 1500)


# Main loop
while True:
	# Check if player wants to exit the game:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			exit()

		if gameActive:
			if event.type == obstacleTimer:
				enemyGroup.add(Enemy(randint(0,2)))

		else:
			if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
				gameActive = True
				startTime = pg.time.get_ticks()
			

	if gameActive:
		screen.blit(skySurface, (0, 0))  # blit puts one surface onto another 
		screen.blit(groundSurface, (0, 300))
		score = displayScore()
		
		# player:
		player.update()
		player.draw(screen)

		# enemies:
		enemyGroup.update()
		enemyGroup.draw(screen)

		# check collisions
		gameActive = collisions()

	else:
		screen.fill((94, 129, 162))
		screen.blit(playerStand, playerStandRect)

		scoreMessage = testFont.render(f"Your score: {score}", False, (111, 196, 169))
		scoreMessageRect = scoreMessage.get_rect(center = (400, 330))
		screen.blit(gameName, gameNameRect)

		if score == 0:
			screen.blit(gameMessage, gameMessageRect)
		else:
			gameMessageRect = gameMessage.get_rect(center=(400, 370))
			screen.blit(gameMessage, gameMessageRect)
			screen.blit(scoreMessage, scoreMessageRect)

	pg.display.update()
	clock.tick(60)