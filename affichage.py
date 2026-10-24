import pygame

joueur_img = pygame.image.load("images/hero1.png")
joueur_img = pygame.transform.scale(joueur_img, (125, 125))
paysage_img = pygame.image.load("images/paysage.jpeg")

slime_img = pygame.image.load("images/slime.png")
slime_img = pygame.transform.scale(slime_img, (125, 125))
slime_img2 = pygame.image.load("images/slime2.png")
slime_img2 = pygame.transform.scale(slime_img2, (125, 125))
slime_img3 = pygame.image.load("images/slime3.png")
slime_img3 = pygame.transform.scale(slime_img3, (150, 150))

fire_img = pygame.image.load("images/fire.png")
fire_img = pygame.transform.scale(fire_img, (100, 100))

fenetre = pygame.display.set_mode((800, 600))
police = pygame.font.SysFont(None, 25)

bouton_vie =  pygame.draw.rect(fenetre, (30,40,40), (50,500,200,60))
bouton_attaque = pygame.draw.rect(fenetre, (30,30,30), (300,500,200,60))
bouton_inventaire = pygame.draw.rect(fenetre, (30,30,30), (550,500,200,60))
texte_attaque = police.render("ameliorer degats",True,(255,255,255))
texte_vie = police.render("ameliorer vie",True,(255,255,255))
texte_inventaire = police.render("inventaire",True,(255,255,255))

def DrawFond():
	fenetre.blit(paysage_img, (0, 0))

def DrawEnnemi(ennemi):
	if ennemi.level == 1:
		fenetre.blit(slime_img, (ennemi.pos[0], ennemi.pos[1]))
	elif ennemi.level == 2:
		fenetre.blit(slime_img2, (ennemi.pos[0], ennemi.pos[1]))
	else:
		fenetre.blit(slime_img3, (ennemi.pos[0], ennemi.pos[1]))
	text1 = police.render(f"PV: {ennemi.vie}", True, (20, 20, 20))
	fenetre.blit(text1, (ennemi.pos[0] + 35, ennemi.pos[1] + 10))

def DrawFire(projectile):
	fire_img2 = pygame.transform.rotate(fire_img, projectile.angle)
	fenetre.blit(fire_img2, (projectile.pos[0] - 50, projectile.pos[1]- 50 ))

def DrawJoueur(pos, hero):
	fenetre.blit(joueur_img, (pos[0], pos[1]))
	text2 = police.render(f"PV: {hero.vie}", True, (20, 20, 20))
	fenetre.blit(text2, (pos[0] + 25, pos[1] - 5))

def DrawUpgrade(bt_vie, bt_attq,bt_inventaire, txt_vie, txt_attq,txt_inventaire):
	pygame.draw.rect(fenetre, (35, 35, 45), (0, 460, 800, 140))
	pygame.draw.rect(fenetre,(50,150,90),bt_vie)
	fenetre.blit(txt_vie,txt_vie.get_rect(center = bt_vie.center))
	pygame.draw.rect(fenetre,(180,80,60),bt_attq)
	fenetre.blit(txt_attq,txt_attq.get_rect(center = bt_attq.center))
	pygame.draw.rect(fenetre,(180,150,60),bt_inventaire)
	fenetre.blit(txt_inventaire,txt_inventaire.get_rect(center = bt_inventaire.center))

def DrawXP():
	pygame.draw.rect(fenetre, (40, 40, 40), (10,10,200,50))
	pygame.draw.rect(fenetre, (80, 1, 47), (15,15,190,40))