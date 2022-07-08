from pygame import sprite, Rect, image

class Enemy(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)

		self.x, self.y, self.speed = 400, 400, 0

		self.player_collision = False

		self.image = image.load("../other/enemyLVL1.png").convert()
		self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

	def update(self, player_pos):
		self.player_posx, self.player_posy = player_pos

		if self.x >= self.player_posx + self.image.get_width():
			self.x -= self.speed
		if self.x <= self.player_posx - self.image.get_width():
			self.x += self.speed
		if self.y >= self.player_posy + self.image.get_height():
			self.y -= self.speed
		if self.y <= self.player_posy - self.image.get_height():
			self.y += self.speed

		if (self.x >= self.player_posx + self.image.get_width() or self.x <= self.player_posx - self.image.get_width())\
		or (self.y >= self.player_posy + self.image.get_height() or self.y <= self.player_posy - self.image.get_height()):
			self.player_collision = True
		else:
			self.player_collision = False

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def p_collision(self):
		return self.player_collision