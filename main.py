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
fire_img = pygame.image.load("images/fire.png")
fire_img = pygame.transform.scale(fire_img, (100, 100))

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
		elif event.type == pygame.MOUSEBUTTONDOWN :
			if event.button == 1 :
				if bouton_vie.collidepoint(event.pos):
					hero1.change_valeur("max_vie",10)
					hero1.change_valeur("vie",10)
					print(f"vie={hero1.vie}")
				elif bouton_attaque.collidepoint(event.pos):
					hero1.change_valeur("attaque",10)
					print(f"att={hero1.attaque}")

	bouton_vie = bouton_attaque = pygame.draw.rect(fenetre, (30,40,40), (60,500,300,60))
	bouton_attaque = bouton_attaque = pygame.draw.rect(fenetre, (30,30,30), (440,500,300,60))

	pygame.draw.rect(fenetre, (35, 35, 45), (0, 460, 800, 140))
	pygame.draw.rect(fenetre,(50,150,90),bouton_vie)
	texte_vie = police.render("ameliorer vie",True,(255,255,255))
	fenetre.blit(texte_vie,texte_vie.get_rect(center = bouton_vie.center))
	pygame.draw.rect(fenetre,(180,80,60),bouton_attaque)
	texte_attaque = police.render("ameliorer degats",True,(255,255,255))
	fenetre.blit(texte_attaque,texte_attaque.get_rect(center = bouton_attaque.center))

	fenetre.blit(joueur_img, (joueur[0], joueur[1]))

	jeu.spawn_ennemie()
	jeu.attaque_hero()
	text2 = police.render(f"PV: {hero1.vie}", True, (20, 20, 20))
	fenetre.blit(text2, (joueur[0] + 25, joueur[1] - 5))
	for i in range (len(jeu.tab_proj)):
		proj = jeu.tab_proj[i]
		# pygame.draw.rect(fenetre, (15, 15, 15), (proj.pos[0],proj.pos[1],10,10))
		fire_img2 = pygame.transform.rotate(fire_img, proj.angle)
		fenetre.blit(fire_img2, (proj.pos[0] - 50, proj.pos[1]- 50 ))

	for i in range(len(jeu.tab)):
		ennemi = jeu.tab[i]
		text1 = police.render(f"PV: {ennemi.vie}", True, (20, 20, 20))
		fenetre.blit(text1, (ennemi.pos[0] + 35, ennemi.pos[1] + 10))
		jeu.action_ennemi(ennemi)
		fenetre.blit(slime_img, (ennemi.pos[0], ennemi.pos[1]))
	pygame.display.flip()


	
clock.tick(60)
pygame.quit()