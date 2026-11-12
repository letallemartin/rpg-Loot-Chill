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

	def AnimeEnnemie(self, ennemi):
		if ennemi.pos[3] >= 75:
			ennemi.change_pos(-1, 3)
		elif ennemi.pos[3] < 25:
			ennemi.change_pos(1, 3)
		print(ennemi.pos[3])

	def action_ennemi(self, ennemi):
            if ennemi.pos[0] >= 150:
                ennemi.change_pos(ennemi.vitesse, 0)
            else:
                temp = pygame.time.get_ticks()
                if temp - ennemi.last_action >= 2000:
                    self.hero.change_valeur("vie", -ennemi.attaque)
                    ennemi.change_temps(temp)

	def spawn_ennemi(self):
		if len(self.tab) < 4:
			x = random.randint(600, 700)
			y = random.randint(50, 350)
			ennemi = self.type_ennemi(x, y)
			self.tab.append(ennemi)

	def type_ennemi(self, x, y):
		luk = random.randint(1,100)
		if 60 <= luk <= 80 and self.hero.xp["niveau"] > 1:
			ennemi = Ennemie(65,5, 0, [x, y, 50, 50], 2, -0.20)
		elif luk > 80 and self.hero.xp["niveau"] > 4:
			ennemi = Ennemie(100,20, 0, [x, y, 50, 50], 3, -0.1)
		else:
			ennemi = Ennemie(40,3, 0, [x, y, 50, 50], 1, -0.3) 
		return ennemi

	def ennemie_proche(self):
		
		cible = self.tab[0]
		for ennemie in self.tab[1:]:
			if ennemie.pos[0] < cible.pos[0]:
				cible = ennemie
		return cible
       
			
	def attaque_hero(self):
		temp = pygame.time.get_ticks()
		if temp - self.hero.last_action >= 1500 and len(self.tab) > 0:
			ennemi_cible = self.ennemie_proche()
			projectile = Projectile([self.hero_pos[0] + self.hero_pos[2], self.hero_pos[1] + 25], 10, ennemi_cible)
			self.tab_proj.append(projectile)
			self.hero.change_temps(temp)
   
		if self.action_projectile():
			for proj in self.tab_proj:
				proj.ennemi_cible.change_valeur("vie", -self.hero.attaque)
				if not self.est_vie(proj.ennemi_cible):
					self.verif_ennemi(proj.ennemi_cible)
					self.tab.remove(proj)

	def action_projectile(self):
		if len(self.tab_proj) > 0:
			for projectile in self.tab_proj:
				projectile.deplace_projectile()
				if projectile.est_touché():
					self.tab_proj.remove(projectile)
					return True

	def verif_ennemi(self, ennemi_cible): #peut etre futur pr global recompenses
		for i in range (1, 4):
			if ennemi_cible.level == i:
				self.hero.change_dico("actuelle", 5 * i)
				self.hero.change_valeur("argent", 5 * i)
		self.hero.verif_level()

	def change_prix(self,bouton):
		bouton["prix"] *= 1.2
		bouton["prix"] = round(bouton["prix"],2)

	def est_argent(self, bouton):
		if self.hero.argent >= bouton["prix"]:
			self.hero.change_valeur("argent", - bouton["prix"])
			return True