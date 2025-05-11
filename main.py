import pygame
from constants import *
from player import Player
def main():
	pygame.init()
	
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	clock = pygame.time.Clock()
	dt = 0
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	player = Player(x, y)


	while True:
		# it will quit the loop if we click on X 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		player.update(dt)
		screen.fill("black")
		player.draw(screen)

		pygame.display.flip()
		# Limit the frame to 60fps
		dt = clock.tick(60) / 1000

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()