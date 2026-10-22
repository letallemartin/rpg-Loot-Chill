from p5 import *
import random
from Ennemie_base import Ennemie
from Hero_base import Hero

class Jeu:
	def __init__(self, tab, hero):
		self.tab = tab
		self.hero = hero
	
	def est_vie(self, perso):
		return perso.vie <= 0

	def action_ennemi(self, en):
		temp = millis()
		if temp - en.last_action >= 1000:
			if en.pos[0] >= 100:
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
		temp = millis()
		if temp - self.hero.last_action >= 1000:
			if len(self.tab) > 0:
				ennemi_cible = self.tab[0]
				ennemi_cible.change_valeur("vie", -self.hero.attaque +9) 
				print(f"pv ennemi : {ennemi_cible.vie}")
				if ennemi_cible.vie <= 0:
					self.tab.pop(0)
			self.hero.change_temps(temp)
			print(f"temp: {temp}, temp - last: {temp - self.hero.last_action}, derniere action: {self.hero.last_action}")
