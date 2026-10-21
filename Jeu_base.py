from p5 import *
class Jeu:
	def __init__(self, tab, hero):
		self.tab = tab
		self.hero = hero
	
	def est_vie(self, perso):
		return perso.vie <= 0

	def action_enemie(self):
		i = 0
		temp = millis()
		for e in self.tab:
			if temp - e.last_action >= 2000:
				if e.pos[1] >= 50:
					e.pos[1] -= 5
					# e.change_valeur(pos, -1)
				else:
					hero.vie -= 5
					# hero.change_valeur(vie, -10)
				e.last_action = temp
				# e.change_valeur(last_action, temp)


		#self.tab self.tab[i].pos[0]

	def action_joueur(self):
		pass

