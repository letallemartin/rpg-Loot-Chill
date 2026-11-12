import math
class Projectile:
	def __init__(self,pos, vitesse, ennemi_cible, angle = 0):
		self.pos = pos #[x, y] joueur
		self.vitesse = vitesse # int
		self.ennemi_cible = ennemi_cible #cible
		self.angle = angle - 45

	def deplace_projectile(self):
		try:
			pente = (self.ennemi_cible.pos[1] - self.pos[1] + 40) / (self.ennemi_cible.pos[0] - self.pos[0] + 40)
			self.pos[0] += 3
			self.pos[1] += pente * 3
			self.angle = - ((math.atan(pente) * 180) / math.pi) # 45 = diff d'angle dui png
		except ZeroDivisionError:
			pass

	def est_touché(self):
		if self.ennemi_cible.pos[0] < self.pos[0] < (self.ennemi_cible.pos[0] + 50) and self.ennemi_cible.pos[1] < self.pos[1] < self.ennemi_cible.pos[1] + 50:
			return True