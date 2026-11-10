import pygame

joueur_img = pygame.image.load("images/hero1.png")
joueur_img = pygame.transform.scale(joueur_img, (150, 150))
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

bouton_maxvie = {"rect":pygame.Rect((300,500,150,60)),"txt": "+ max vie","prix":10,"couleur":(50,150,90)}
bouton_attaque = {"rect":pygame.Rect((500,500,150,60)),"txt" :"+ degats","prix":10,"couleur":(180,80,60)}
bouton_vie = {"rect":pygame.Rect((100,500,150,60)),"txt" :"heal","prix":100,"couleur": (27,10,150)}

liste_bt =[bouton_maxvie,bouton_attaque,bouton_vie]

xp_cadre = pygame.image.load("images/xp_cadre.png")
xp_cadre = pygame.transform.scale(xp_cadre, (210, 210))

gold_img = pygame.image.load("images/ui_xp2.png") # a modif nom png
gold_img = pygame.transform.scale(gold_img, (80, 45))

def DrawFond():
	fenetre.blit(paysage_img, (0, 0))

def DrawEnnemi(ennemi):
	if ennemi.level == 1:
		fenetre.blit(slime_img, (ennemi.pos[0], ennemi.pos[1]))
	elif ennemi.level == 2:
		fenetre.blit(slime_img2, (ennemi.pos[0], ennemi.pos[1]))
	else:
		fenetre.blit(slime_img3, (ennemi.pos[0], ennemi.pos[1]))
	text1 = police.render(f"PV: {ennemi.vie}", True, (0,0,0))
	fenetre.blit(text1, (ennemi.pos[0] + 35, ennemi.pos[1] + 10))


def DrawFire(projectile):
	fire_img2 = pygame.transform.rotate(fire_img, projectile.angle)
	fenetre.blit(fire_img2, (projectile.pos[0] - 50, projectile.pos[1]- 50 ))

def DrawJoueur(pos, hero):
	fenetre.blit(joueur_img, (pos[0], pos[1]))
	text2 = police.render(f"PV: {hero.vie}", True, (0,0,0))
	fenetre.blit(text2, (pos[0] + 35, pos[1] - 5))

def DrawUpgrade(liste_bt):
	pygame.draw.rect(fenetre, (35, 35, 45), (0, 460, 800, 140))
	for bouton in liste_bt:
		pygame.draw.rect(fenetre,bouton["couleur"],bouton["rect"])
		affi_prix = f"{bouton['txt']}   {bouton['prix']} $"
		affi_txt = police.render(affi_prix,True,(255,255,255))
		fenetre.blit(affi_txt, affi_txt.get_rect(center = bouton["rect"].center))

def DrawXP(hero):
	txt_xp = police.render(str(hero.xp["niveau"]),True,(0,0,0)) 
	progression = 150 * hero.xp["actuelle"] / hero.xp["max"]
	pygame.draw.rect(fenetre, (18, 243, 18), (32,25,progression,26))
	fenetre.blit(xp_cadre, (0,-70))
	fenetre.blit(txt_xp,(100,29))
 
def DrawArgent(hero):
    txt_argent = police.render(str(round(hero.argent, 1)),True,(0,0,0))
    fenetre.blit(gold_img, (640,0))
    fenetre.blit(txt_argent,(702,15))