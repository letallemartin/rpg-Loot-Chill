class Projectile:
	def __init__(self,pos, vitesse, pos_cible):
		self.pos = pos #[x, y] joueur
		self.vitesse = vitesse # int
		self.pos_cible = pos_cible #[x, y]
		# self.etat_actif = etat_actif # true false
	
	def deplace_projectile(self):
		pass

	def est_touché(self):
		pass