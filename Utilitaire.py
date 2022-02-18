from turtle import *
import random

colormode(255)
# Fonction qui permet le random des couleurs :
def color():
    return[random.randint(0 ,255),random.randint(0 ,255),random.randint(0 ,255)]

# Fonction qui permet le random des etages:
def rde():
    return random.randint(0,6)

# Fonction qui permet le random des positions de porte:
def rdp():
    return random.randint(0,3)

# Fonction qui permet le random des fentres:
def rd():
    return random.randint(0, 100)

# Fonction qui permet le random des positions :
def posi(x, y):
    return random.randint(x, y)

# Fonction qui permet la création de la route :
def route():
    pensize(5)
    goto(1000,0)
    pd()
    goto(-1000,0)
    pensize(1)
    pu()

# Fonction qui permet la création de la route pour les voiture :
def rv():
    pensize(5)
    goto(1000,-113)
    pd()
    goto(-1000,-113)
    pensize(1)
    pu()

# Fonction qui permet la création des étoiles :
def stars():
    pu()
    begin_fill()
    fillcolor("yellow") 
    for i in range (6):
        forward(10)
        left(60)
        forward(10)
        right(120)
    end_fill()

# Fonction qui permet la création de la lune:
def lune():
    goto (-650, 300)
    pu()
    begin_fill()
    fillcolor('#A1A4A4')
    left(90)
    circle(50)
    end_fill()

# Fonction qui permet la création de la voiture :
def voiture():
# Base de la voiture (rectangle):
    color_v = color()
    begin_fill()
    fillcolor(color_v)
    pd()
    pensize(1)
    fd(140)
    left(90)
    fd(30)
    left(90)
    fd(140)
    left(90)
    fd(30)
    end_fill()
# Vitre
    back(30)
    left(90)
    fd(15)
    pensize(2)
    left(45)
    fd(40)
    right(45)
    fd(45)
    right(45)
    fd(40)
    pensize(1)
    left(45)
    fd(23)
    right(90)
# Phare
    begin_fill()
    fillcolor('yellow')
    for i in range(4):
        fd(10)
        right(90)
    end_fill()
# Roue
    fd(30)
    right(90)
    fd(30)
    left(90)
    fd(15)
    left(90)
    begin_fill()
    fillcolor('black')
    circle(12)
    end_fill()
    penup()
    backward(80)
    pd()
    begin_fill()
    circle(12)
    end_fill()
    pu()