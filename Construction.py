from Ouverture import *
from Immeuble import *
from Utilitaire import *

def fond():
    pu()
# Le ciel :
    begin_fill()
    fillcolor('#000D60')
    goto(1000,0)
    goto(1000,1000)
    goto(-1000,1000)
    goto(-1000,0)
    end_fill()

# L'herbe :
    begin_fill()
    fillcolor('#2F6135')
    goto(1000,0)
    goto(1000,-1000)
    goto(-1000,-1000)
    goto(-1000,0)
    end_fill()

# Fonction pour construire des immeubles de tailles différentes:
def immeuble() :
# Fait juste le rez de chausser et le toit:
    if rde() == 1 :
        color_b = color()
        bas(color_b)
        toit()
# Fait le rez de chausser, un étage et le toit:
    elif rde == 2:
        color_b = color()
        bas(color_b)
        mur(color_b)
        fenetre()
        toit()
# Fait le rez de chausser, deux étages et le toit:
    elif rde() == 3:
        color_b = color()
        bas(color_b)
        for i in range(1):
            mur(color_b)
            fenetre()
        toit()
# Fait le rez de chausser, trois étages et le toit:
    elif rde() == 4:
        color_b = color()
        bas(color_b)
        for i in range(2):
            mur(color_b)
            fenetre()
        toit()
# Fait le rez de chausser, quatre étages et le toit:
    elif rde() == 5:
        color_b = color()
        bas(color_b)
        for i in range(3):
            mur(color_b)
            fenetre()
        toit()    
# Fait le rez de chausser, cinq étages et le toit:
    else :
        color_b = color()
        bas(color_b)
        for i in range(4):
            mur(color_b)
            fenetre()
        toit()

# Fonction qui permet de construire les 6 immeubles et la route :
def contruction () :
    speed(0)
    fond()
    route()
# Permet la construction aléatoire des etoiles :
    for i in range (0,10) :
        if rd() < 50 :
            posi1 = posi(0,700)
        else :
            posi1 = posi(-700,0)
        posi2 = posi(340,550)
        pu()
        setpos(posi1, posi2)
        stars()
# Permet la construction aléatoire des immeubles :
    for i in range(0, 6):
        penup()
        goto (-500, 0)
        forward(i*180)
        immeuble()
# Construit deux voiture a des positions definit :
    pu()
    rv()
    setpos(200,-100)
    voiture()
    setpos(-300,-100)
    voiture()
    lune()
    hideturtle()


contruction()


mainloop()