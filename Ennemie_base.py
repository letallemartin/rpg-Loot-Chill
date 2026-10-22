from p5 import *
class Ennemie:
	def __init__(self, vie, max_vie, attaque, last_action,pos):
		self.vie = vie
		self.max_vie = max_vie
		self.attaque = attaque
		self.last_action = last_action
		self.pos = pos #liste [x, y, x taille, y taille]

	def change_valeur(self,valeur, new): # vie / attaque / max_vie 
			act = getattr(self, valeur)
			setattr(self, valeur, act + new)
	
	def change_pos(self, valeur, indice): #pos
		self.pos[indice] += valeur
	
	def change_temps(self, new): #temp
		self.last_action = new
	
	def __str__(self):
		return f"{self.pos}"