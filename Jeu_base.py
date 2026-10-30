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

	# def AnimeEnnemie(self, ennemi):
	# 	if ennemi.pos[3] >= 75:
	# 		ennemi.change_pos(-1, 3)
	# 	elif ennemi.pos[3] < 25:
	# 		ennemi.change_pos(1, 3)
	# 	print(ennemi.pos[3])

	def action_ennemi(self, en):
			if en.pos[0] >= 150:
				en.change_pos(en.vitesse, 0)
			else:
				temp = pygame.time.get_ticks()
				if temp - en.last_action >= 2000:
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
			ennemi = Ennemie(40,3, 0, [x, y, 50, 50], 1, -0.4)
		elif luk <= 80:
			ennemi = Ennemie(65,5, 0, [x, y, 50, 50], 2, -0.35)
		else:
			ennemi = Ennemie(100,20, 0, [x, y, 50, 50], 3, -0.2)
		return ennemi
	
	def attaque_hero(self):
		temp = pygame.time.get_ticks()
		ennemi_cible = self.tab[0] # à changer !!!
		if temp - self.hero.last_action >= 3000 and len(self.tab) > 0:
			proj = Projectile([self.hero_pos[0] + self.hero_pos[2], self.hero_pos[1] + 25], 10, [ennemi_cible.pos[0], ennemi_cible.pos[1]])
			self.tab_proj.append(proj)
			self.hero.change_temps(temp)
		if self.action_projectile():
			ennemi_cible.change_valeur("vie", -self.hero.attaque)
			if not self.est_vie(ennemi_cible):
				self.verif_ennemi(ennemi_cible)
				self.tab.remove(ennemi_cible)

	def action_projectile(self):
		if len(self.tab_proj) > 0:
			for pr in self.tab_proj:
				pr.deplace_projectile()
				if pr.est_touché():
					self.tab_proj.remove(pr)
					return True

	def verif_ennemi(self, ennemi_cible): #peut etre futur pr global recompenses
		for i in range (1, 4):
			if ennemi_cible.level == i:
				self.hero.change_dico("actuelle", 5 * i)
				self.hero.change_valeur("argent", 5 * i)
		self.hero.verif_level()

	def est_argent(self, bouton):
		if self.hero.argent >= bouton["prix"]:
			bouton["prix"] *= 1.2
			return True