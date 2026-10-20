from p5 import *
joueur = [100,100,50,50]
def setup():
	size(800, 550)

def draw():
	background(204)
	rect((joueur[0], joueur[1]), joueur[2], joueur[2])

