from pygame import sprite, image, Rect
from globals import bullet_speed

class Bullet(sprite.Sprite):
	def __init__(self, shoot_r, shoot_l, shoot_u, shoot_d, player_pos, player_size):
		sprite.Sprite.__init__(self)

		self.speed = bullet_speed

		self.pw, self.ph = player_size
		self.x, self.y = player_pos
		self.x += self.pw / 2
		self.y += self.ph / 2

		self.range_time = 0
		self.range = 25

		self.shoot_r, self.shoot_l, self.shoot_u, self.shoot_d = shoot_r, shoot_l, shoot_u, shoot_d

		self.image = image.load("../other/bullet.png").convert_alpha()
		self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

	def update(self):
		if self.shoot_r and self.shoot_l:
			self.x += self.speed
		if self.shoot_u and self.shoot_d:
			self.y += self.speed

		if self.shoot_r:
			self.x += self.speed
		if self.shoot_l:
			self.x -= self.speed
		if self.shoot_u:
			self.y -= self.speed
		if self.shoot_d:
			self.y += self.speed

		self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

		if self.range_time >= self.range - 10:
			self.y += 1

		self.remove()

	def remove(self):
		self.range_time += 1
		if self.range_time >= self.range:
			self.kill()
			self.range_time = 0