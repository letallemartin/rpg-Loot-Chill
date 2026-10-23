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
		# print(f"temp: {temp}, ecart: {temp - en.last_action}, derniere action: {en.last_action}")

	def spawn_ennemie(self):
		if len(self.tab) < 4:
			x = random.randint(600, 700)
			y = random.randint(50, 400)
			ennemie = Ennemie(50, 50,10, 0, [x, y, 50, 50])
			self.tab.append(ennemie)
			print(ennemie)

	

	def attaque_hero(self):
		temp = pygame.time.get_ticks()
		if temp - self.hero.last_action >= 3000 and len(self.tab) > 0:
			ennemi_cible = self.tab[0]
			proj = Projectile([self.hero_pos[0] + self.hero_pos[2], self.hero_pos[1] + 25], 10, [ennemi_cible.pos[0], ennemi_cible.pos[1]])
			self.tab_proj.append(proj)
			print(f"pv ennemi : {ennemi_cible.vie}")
			self.hero.change_temps(temp)
			print(f"temp: {temp}, temp - last: {temp - self.hero.last_action}, derniere action: {self.hero.last_action}")
		self.action_projectile()
		if not self.est_vie(self.tab[0]):
			self.tab.pop(0)

	def action_projectile(self):
		if len(self.tab_proj) > 0:
			for pr in self.tab_proj:
				pr.deplace_projectile()
				if pr.est_touché():
					self.tab[0].change_valeur("vie", -self.hero.attaque)
					self.tab_proj.remove(pr)




# def attaque_hero(self):
# 		temp = millis()
# 		if temp - self.hero.last_action >= 1000 and len(self.tab) > 0::
# 			ennemi_cible = self.tab[0]
# 			ennemi_cible.change_valeur("vie", -self.hero.attaque + 9)
# 			print(f"pv ennemi : {ennemi_cible.vie}")
# 			if not est_vie(ennemi_cible) <= 0:
# 				self.tab.pop(0)
# 			self.hero.change_temps(temp)
# 			print(f"temp: {temp}, temp - last: {temp - self.hero.last_action}, derniere action: {self.hero.last_action}")