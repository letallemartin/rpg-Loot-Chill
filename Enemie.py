def Enemie:
	def __init__(self, vie, max_vie, attaque, argent, last_attaque):
		self.vie = vie
		self.max_vie = max_vie
		self.attaque = attaque
		self.last_attaque = last_attaque

	def change_valeur(self,valeur, new):
		act = getattr(self, valeur)
		setattr(self, valeur, act + new)