import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()	
	drawable = pygame.sprite.Group()	
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# this ensures that every instance of the asteroid class is automatically added to these groups upon creation
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	Player.containers = (updatable,drawable)

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	dt = 0
	

	player = Player(x, y)


	while True:
		# it will quit the loop if we click on X 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split()
					shot.kill()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)
		

		pygame.display.flip()
		# Limit the frame to 60fps
		dt = clock.tick(60) / 1000

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()