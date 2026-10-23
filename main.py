import pygame
from Jeu_base import Jeu
from Hero_base import Hero
from Ennemie_base import Ennemie
pygame.init()
import affichage 
joueur = [50,200,50,50]
hero1 = Hero(100,100,10,1000,0)
jeu = Jeu([], hero1, [joueur[0], joueur[1], joueur[2], joueur[3]], [])

running = True

clock = pygame.time.Clock()


while running:
	affichage.DrawFond()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN :
			if event.button == 1 :
				if affichage.bouton_vie.collidepoint(event.pos):
					hero1.change_valeur("max_vie",10)
					hero1.change_valeur("vie",10)
					print(f"vie={hero1.vie}")
				elif affichage.bouton_attaque.collidepoint(event.pos):
					hero1.change_valeur("attaque",10)
					print(f"att={hero1.attaque}")
	affichage.DrawUpgrade(affichage.bouton_vie, affichage.bouton_attaque, affichage.texte_vie, affichage.texte_attaque)
	affichage.DrawJoueur(joueur, hero1)
	jeu.spawn_ennemie()
	jeu.attaque_hero()
	for i in range (len(jeu.tab_proj)):
		proj = jeu.tab_proj[i]
		affichage.DrawFire(proj)
	for i in range(len(jeu.tab)):
		ennemi = jeu.tab[i]
		jeu.action_ennemi(ennemi)
		affichage.DrawEnnemi(ennemi)
	pygame.display.flip()


	
clock.tick(60)
pygame.quit()