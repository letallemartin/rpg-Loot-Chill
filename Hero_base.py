class Hero:
	def __init__(self, vie, max_vie, attaque, argent, last_action, xp = {"niveau": 0, "actuelle": 0, "max": 100}):
		self.vie = vie #int
		self.max_vie = max_vie #int
		self.attaque = attaque #int
		self.argent = argent #int
		self.last_action = last_action
		self.xp = xp #dico

	def change_valeur(self,valeur, new):
		act = getattr(self, valeur)
		setattr(self, valeur, act + new)

	def change_temps(self, new): #temp
		self.last_action = new

	def change_dico(self, cle, new):
		self.xp[cle] += new

	def verif_level(self):
		for v,x in self.xp.items():
			print("cl: ",v,"al",x)
		if self.xp["actuelle"] >  self.xp["max"]:
			self.xp["niveau"] += 1
			self.xp["actuelle"] -= self.xp["max"] #pr garder le surplu d'xp (ex 130 xp = 30xp et 1 niv)