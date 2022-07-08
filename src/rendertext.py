import pygame

class RenderText:
	def __init__(self):
		self.font = pygame.font.SysFont('../other/HyperStiffRoundBootiedOpossumRegular-XjVd.ttf', 30)
	def update(self, text, pos, screen):
		self.text = self.font.render(f"{text}", False, (0, 255, 0))
		screen.blit(self.text, pos)