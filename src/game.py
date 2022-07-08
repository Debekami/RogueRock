from pygame import sprite, image, sprite
from o_player import *
from o_bullet import *
from globals import *
from o_enemy import *
from rendertext import RenderText
from threading import Thread

class Lvl1:
	def __init__(self):
		self.enemy, self.enemy.speed = Enemy(), enemy_speed
		self.background = image.load("../other/lvl1.png").convert()

	def update(self, screen, player):
		screen.blit(self.background, (0, 0))
		self.enemy.update(player.pos())
		self.enemy.draw(screen)

class Game:
	def __init__(self):
		self.player, self.hp, self.bullets, self.lvl1, self.renderfps, self.renderavgfps, self.player.speed = Player(), Hp(), sprite.Group(), Lvl1(), RenderText(), RenderText(), player_speed
		self.cooldown, self.avg, self.avgl = 0, 0, []

	def update(self, clock):

		self.pThread = Thread(target = self.player.update, args = (self.lvl1.enemy.p_collision(),))
		self.pThread.start()

		self.hp.update()
		self.bullets.update()

		self.shoot_r, self.shoot_l, self.shoot_u, self.shoot_d = self.player.shoot()

		if self.cooldown >= 10:
			if self.shoot_r or self.shoot_l or self.shoot_u or self.shoot_d:
				self.bullets.add(Bullet(self.shoot_r, self.shoot_l, self.shoot_u, self.shoot_d, self.player.pos(), self.player.size()))
				self.cooldown = 0
		else:
			self.cooldown += 1

		self.avgl.append(int(clock.get_fps()))
		self.avg = sum(self.avgl) / len(self.avgl)

	def draw(self, screen, clock):
		self.lvl1.update(screen, self.player)

		self.player.draw(screen)
		self.hp.draw(screen)
		self.bullets.draw(screen)
		self.renderfps.update(int(clock.get_fps()), (0, 0), screen)
		self.renderavgfps.update(int(self.avg), (30, 0), screen)