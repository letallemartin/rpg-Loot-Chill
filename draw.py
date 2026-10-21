from p5 import *
from Jeu_base import Jeu
from Hero_base import Hero
from Ennemie_base import Ennemie

joueur = [100,100,50,50]
ennemi1 = Ennemie(100, 100, 5, 15, 0, [500, 150, 50, 50])
ennemi2 = Ennemie(100, 100, 5, 15, 0, [500, 250, 50, 50])
hero1 = Hero(100,100,10,1000,0)
jeu = Jeu([ennemi1,ennemi2], hero1)

def setup():
	size(800, 550)

def draw():
	background(204)
	rect((joueur[0], joueur[1]), joueur[2], joueur[2])
	for i in range(len(jeu.tab)):
		ennemi = jeu.tab[i]
		jeu.action_enemie()
		rect(ennemi.pos[0],ennemi.pos[1])

def mouse_pressed():
	pass

run(renderer = "skia")
