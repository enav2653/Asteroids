import pygame
from circleshape import CircleShape
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2), PLAYER_RADIUS)
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updateable.update(dt)
		screen.fill("black")

		for sprite in drawable:
			sprite.draw(screen)

		pygame.display.flip()
		dt = Clock.tick(60)/1000 #limit framerate to 60 FPS

if __name__ == "__main__":
    main()
