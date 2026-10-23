import pygame
from Jeu_base import Jeu
from Hero_base import Hero
from Ennemie_base import Ennemie

joueur = [50,200,50,50]
hero1 = Hero(100,100,10,1000,0)
jeu = Jeu([], hero1, [joueur[0], joueur[1], joueur[2], joueur[3]], [])

joueur_img = pygame.image.load("images/hero1.png")
joueur_img = pygame.transform.scale(joueur_img, (125, 125))
paysage_img = pygame.image.load("images/paysage.jpeg")
slime_img = pygame.image.load("images/slime.png")
slime_img = pygame.transform.scale(slime_img, (125, 125))

running = True
pygame.init()
fenetre = pygame.display.set_mode((800, 600))
police = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()

while running:
	fenetre.blit(paysage_img, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	fenetre.blit(joueur_img, (joueur[0], joueur[1]))

	jeu.spawn_ennemie()
	jeu.attaque_hero()
	text2 = police.render(f"PV: {hero1.vie}", True, (20, 20, 20))
	fenetre.blit(text2, (joueur[0] + 25, joueur[1] - 5))
	for i in range (len(jeu.tab_proj)):
		proj = jeu.tab_proj[i]
		pygame.draw.rect(fenetre, (15, 15, 15), (proj.pos[0],proj.pos[1],10,10))

	for i in range(len(jeu.tab)):
		ennemi = jeu.tab[i]
		text1 = police.render(f"PV: {ennemi.vie}", True, (20, 20, 20))
		fenetre.blit(text1, (ennemi.pos[0] + 35, ennemi.pos[1] + 10))
		jeu.action_ennemi(ennemi)
		fenetre.blit(slime_img, (ennemi.pos[0], ennemi.pos[1]))
	pygame.display.flip()
	
clock.tick(60)
pygame.quit()

