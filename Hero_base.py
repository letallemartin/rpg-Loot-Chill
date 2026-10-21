class Hero:
	def __init__(self, vie, max_vie, attaque, argent, last_action):
		self.vie = vie
		self.max_vie = max_vie
		self.attaque = attaque
		self.argent = argent
		self.last_action = last_action

	def change_valeur(self,valeur, new):
		act = getattr(self, valeur)
		setattr(self, valeur, act + new)
	
	def est_vie(self, objet):
		return objet.vie <= 0

	

