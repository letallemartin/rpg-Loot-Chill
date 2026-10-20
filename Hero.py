class Hero:
	def __init__(self, vie, max_vie, attaque, argent, last_attaque, pos):
		self.vie = vie
		self.max_vie = max_vie
		self.attaque = attaque
		self.argent = argent
		self.last_attaque = last_attaque
		self.pos = pos

	def change_valeur(self,valeur, new):
		act = getattr(self, valeur)
		setattr(self, valeur, act + new)

	
hero1 = Hero(100, 100, 10, 10, 0, [50, 50, 50, 50])
print(hero1.vie)
hero1.change_valeur("vie", 10)
print(hero1.vie)