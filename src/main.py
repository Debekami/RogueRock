import pygame
import sys

pygame.font.init()

from globals import *
from game import Game
from rendertext import RenderText


class Menu:
	def __init__(self):
		self.title = RenderText()
		self.play = RenderText()
		self.settings = RenderText()
		self.exit = RenderText()
		self.tPlay = "Play"
		self.tSet = "Settings"
		self.tExit = "Exit"
		self.current = 1
		self.cooldown = 0
		self.gameLoop = 0
		self.menuLoop = 1

	def update(self):
		key = pygame.key.get_pressed()

		if self.cooldown >= 10:
			if self.current <= 2:
				if key[pygame.K_DOWN]:
					self.current += 1
			if key[pygame.K_UP]:
				if self.current >= 1:
					self.current -= 1

		if self.current == 1:
			self.tPlay = "-> Play"
			self.tSet = "Settings"
			self.tExit = "Exit"

			if key[pygame.K_RETURN]:
				self.gameLoop = 1
				self.menuLoop = 0

		if self.current == 2:
			self.tPlay = "Play"
			self.tSet = "-> Settings"
			self.tExit = "Exit"

		if self.current == 3:
			self.tPlay = "Play"
			self.tSet = "Settings"
			self.tExit = "-> Exit"

		
		self.cooldown += 1

	def draw(self, screen):
		self.title.update("Rogue Rock", (100, 100), screen)
		self.play.update(self.tPlay, (100, 200), screen)
		self.settings.update(self.tSet, (100, 250), screen)
		self.exit.update(self.tExit, (100, 350), screen)

if __name__ == "__main__":
	pygame.init()

	screen = pygame.display.set_mode((500, 500), flags = pygame.SCALED | pygame.FULLSCREEN | pygame.DOUBLEBUF | 1, vsync=1)
	pygame.display.set_caption("RogueRock")
	pygame.mouse.set_visible(False)

	game = Game()
	menu = Menu()

	running = 1

	gameLoop = 0
	menuLoop = 1

	clock = pygame.time.Clock()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0

		screen.fill((0,0,0))

		if menuLoop:
			menu.update()
			menu.draw(screen)
			menuLoop = menu.menuLoop
			gameLoop = menu.gameLoop
		if gameLoop:
			game.update(clock)
			game.draw(screen, clock)

		pygame.display.flip()
		clock.tick(50)

sys.exit()