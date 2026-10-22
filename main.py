import pygame
from Jeu_base import Jeu
from Hero_base import Hero
from Ennemie_base import Ennemie

joueur = [50,100,50,50]
hero1 = Hero(100,100,10,1000,0)
jeu = Jeu([], hero1)

running = True
pygame.init()
fenetre = pygame.display.set_mode((800, 600))
police = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()

while running:
	fenetre.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.draw.rect(fenetre,(30, 30, 30),(joueur[0], joueur[1], joueur[2], joueur[2]))

	jeu.spawn_ennemie()
	jeu.attaque_hero()
	text2 = police.render(f"PV: {hero1.vie}", True, (20, 20, 20))
	fenetre.blit(text2, (joueur[0], joueur[1] - 15))

	for i in range(len(jeu.tab)):
		ennemi = jeu.tab[i]
		text1 = police.render(f"PV: {ennemi.vie}", True, (20, 20, 20))
		fenetre.blit(text1, (ennemi.pos[0], ennemi.pos[1] - 15))
		jeu.action_ennemi(ennemi)
		pygame.draw.rect(fenetre,(50, 50, 50),(ennemi.pos[0],ennemi.pos[1],50,50))
	pygame.display.flip()
	
clock.tick(60)
pygame.quit()

police(f"PV: {ennemi.vie}", ennemi.pos[0], ennemi.pos[1] - 5)