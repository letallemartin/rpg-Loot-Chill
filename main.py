import pygame
from Jeu_base import Jeu
from Hero_base import Hero
from Ennemie_base import Ennemie
pygame.init()
import affichage

joueur = [50,200,75,75]
hero1 = Hero(100,100,10,1000,0)
jeu = Jeu([], hero1, [joueur[0], joueur[1], joueur[2], joueur[3]], [])

running = True

clock = pygame.time.Clock()

while running:
	affichage.DrawFond()
	print("martin retardataire")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN :
			if event.button == 1 :
				if affichage.liste_bt[0]["rect"].collidepoint(event.pos)and jeu.est_argent(affichage.liste_bt[0]): #bouton vie +
					hero1.change_valeur("max_vie",10)
					hero1.change_valeur("vie",10)
					print(f"vie={hero1.vie}")
				elif affichage.liste_bt[1]["rect"].collidepoint(event.pos)and jeu.est_argent(affichage.liste_bt[1]): #bouton attaque +
					hero1.change_valeur("attaque",10)
					hero1.argent -= 10
					print(f"att={hero1.attaque}")
				elif affichage.liste_bt[2]["rect"].collidepoint(event.pos):
					print(f"inv=oui")

	jeu.spawn_ennemi()
	jeu.attaque_hero()
	for i in range (len(jeu.tab_proj)):
		proj = jeu.tab_proj[i]
		affichage.DrawFire(proj)
	for i in range(len(jeu.tab)):
		ennemi = jeu.tab[i]
		jeu.action_ennemi(ennemi)
		affichage.DrawEnnemi(ennemi)
	
	affichage.DrawUpgrade(affichage.liste_bt)
	affichage.DrawJoueur(joueur, hero1)
	affichage.DrawXP(hero1)
	
	pygame.display.flip()
pygame.quit()