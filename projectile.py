import math
class Projectile:
	def __init__(self,pos, vitesse, pos_cible, angle = 0):
		self.pos = pos #[x, y] joueur
		self.vitesse = vitesse # int
		self.pos_cible = pos_cible #[x, y]
		self.angle = angle - 45

	def deplace_projectile(self):
		try:
			pente = (self.pos_cible[1] - self.pos[1] + 25) / (self.pos_cible[0] - self.pos[0] + 25)
			self.pos[0] += 2
			self.pos[1] += pente * 2
			self.angle = - ((math.atan(pente) * 180) / math.pi) # 45 = diff d'angle dui png
		except ZeroDivisionError:
			pass

	def est_touché(self):
		if self.pos_cible[0] < self.pos[0] < (self.pos_cible[0] + 50) and self.pos_cible[1] < self.pos[1] < self.pos_cible[1] + 50:
			return True
