from pygame import sprite, image, key
from pygame.locals import K_w, K_s, K_a, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT

class Player(sprite.Sprite):
	def __init__(self):
		self.speed = 0

		self.image = image.load("../other/player.png").convert()

		self.x, self.y = 250 - self.image.get_width() / 2, 250 - self.image.get_height() / 2

		self.shoot_r, self.shoot_l, self.shoot_u, self.shoot_d = False, False, False, False

	def update(self, collision):
		keys = key.get_pressed()

		self.collision = collision

		# movement

		self.y -= self.speed if keys[K_w] else False
		self.y += self.speed if keys[K_s] else False
		self.x -= self.speed if keys[K_a] else False
		self.x += self.speed if keys[K_d] else False

		# map border

		if self.x <= 50:
			self.x = 50
		if self.x + self.image.get_width() >= 450:
			self.x = 450 - self.image.get_width()
		if self.y <= 50:
			self.y = 50
		if self.y + self.image.get_height() >= 450:
			self.y = 450 - self.image.get_height()

		# shooting

		if keys[K_RIGHT]:
			self.shoot_r = True
		else:
			self.shoot_r = False
		if keys[K_LEFT]:
			self.shoot_l = True
		else:
			self.shoot_l = False
		if keys[K_UP]:
			self.shoot_u = True
		else:
			self.shoot_u = False
		if keys[K_DOWN]:
			self.shoot_d = True
		else:
			self.shoot_d = False

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def pos(self):
		return self.x, self.y
	def size(self):
		return self.image.get_width(), self.image.get_height()

	def shoot(self):
		return self.shoot_r, self.shoot_l, self.shoot_u, self.shoot_d

class Hp(sprite.Sprite):
	def __init__(self):
		self.image = image.load("../other/heart.png")
		self.x = 50
		self.y = 18

	def update(self):
		pass

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
		screen.blit(self.image, (self.x + self.image.get_width(), self.y))