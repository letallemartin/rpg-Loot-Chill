from p5 import *
class Ennemie:
	def __init__(self, vie, max_vie, attaque, argent, last_action,pos):
		self.vie = vie
		self.max_vie = max_vie
		self.attaque = attaque
		self.last_action = last_action
		self.pos = pos #liste [x, y, x taille, y taille]

	def change_valeur(self,valeur, new):
			act = getattr(self, valeur)
			setattr(self, valeur, act + new)
	
	def change_pos(self, valeur, indice):
		self.pos[indice] += valeur