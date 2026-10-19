from p5 import *

carre1 = [100, 100, 200, 80]
carre2 = [350, 300, 200, 80]
carre3 = [50, 300, 200, 80]
vitesse = 10
etat = 'top'
def setup():
    size(800, 550)

def draw():
    global vitesse, etat
    background(204)

    ellipse((mouse_x, mouse_y), 18, 18)
    rect((carre1[0], carre1[1]), carre1[2], carre1[3])
    rect((carre2[0], carre2[1]), carre2[2], carre2[3])
    rect((carre3[0], carre3[1]), carre3[2], carre3[3])
    if etat == 'bounce':
        carre1[0] += vitesse
        vitesse = vitesse * 0.9
        if vitesse <= 1 and vitesse > 0:
            etat = 'top'

def mouse_pressed():
    global vitesse, etat
    if carre2[0] <= mouse_x <= carre2[0] + carre2[2] and carre2[1] <= mouse_y <= carre2[1] + carre2[3]:
        etat = 'bounce'
        vitesse = 10
    if carre3[0] <= mouse_x <= carre3[0] + carre3[2] and carre3[1] <= mouse_y <= carre3[1] + carre3[3]:
        etat = 'bounce'
        vitesse = -10


run(renderer="skia")