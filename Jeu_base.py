import pygame
import random
from Ennemie_base import Ennemie
from Hero_base import Hero
from projectile import Projectile

class Jeu:
	def __init__(self, tab, hero, hero_pos, tab_proj):
		self.tab = tab
		self.hero = hero
		self.hero_pos = hero_pos
		self.tab_proj = tab_proj

	def est_vie(self, perso):
		return perso.vie > 0

	def action_ennemi(self, en):
		temp = pygame.time.get_ticks()
		if temp - en.last_action >= 1000:
			if en.pos[0] >= 150:
				en.change_pos(-25, 0)
			else:
				self.hero.change_valeur("vie", -en.attaque)
			en.change_temps(temp)

	def spawn_ennemi(self):
		if len(self.tab) < 4:
			x = random.randint(600, 700)
			y = random.randint(50, 350)
			ennemi = self.type_ennemi(x, y)
			self.tab.append(ennemi)

	def type_ennemi(self, x, y):
		luk = random.randint(1,100)
		if luk <= 60:
			ennemi = Ennemie(40,10, 0, [x, y, 50, 50], 1)
		elif luk <= 80:
			ennemi = Ennemie(65,10, 0, [x, y, 50, 50], 2)
		else:
			ennemi = Ennemie(100,10, 0, [x, y, 50, 50], 3)
		return ennemi


	def attaque_hero(self):
		temp = pygame.time.get_ticks()
		if temp - self.hero.last_action >= 3000 and len(self.tab) > 0:
			ennemi_cible = self.tab[0]
			proj = Projectile([self.hero_pos[0] + self.hero_pos[2], self.hero_pos[1] + 25], 10, [ennemi_cible.pos[0], ennemi_cible.pos[1]])
			self.tab_proj.append(proj)
			self.hero.change_temps(temp)
		if self.action_projectile():
			self.tab[0].change_valeur("vie", -self.hero.attaque)
			if not self.est_vie(self.tab[0]):
				self.verif_xp(self.tab[0])
				self.tab.pop(0)


	def action_projectile(self):
		if len(self.tab_proj) > 0:
			for pr in self.tab_proj:
				pr.deplace_projectile()
				if pr.est_touché():
					self.tab_proj.remove(pr)
					return True

	def verif_xp(self, ennemi_cible): #peut etre futur pr global recompenses
		if ennemi_cible.level == 1:
			self.hero.change_dico("actuelle", 5)
		elif ennemi_cible.level == 2:
			self.hero.change_dico("actuelle", 10)
		elif ennemi_cible.level == 3:
			self.hero.change_dico("actuelle", 20)
		self.hero.verif_level()