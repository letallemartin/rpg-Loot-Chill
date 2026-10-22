from p5 import *
class Jeu:
	def __init__(self, tab, hero):
		self.tab = tab
		self.hero = hero
	
	def est_vie(self, perso):
		return perso.vie <= 0

	def action_ennemi(self, en):
		temp = millis()
		if temp - en.last_action >= 2000:
			if en.pos[0] >= 50:
				en.change_pos(-5, 0)
				print(en.pos[0])
			else:
				self.hero.change_valeur("vie", -10)
			en.change_valeur("last_action", temp)

		#self.tab self.tab[i].pos[0]
	

