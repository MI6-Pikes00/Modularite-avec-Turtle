from Utilitaire import *
from Ouverture import *

def bas(color_b):
    begin_fill()
    fillcolor(color_b)
    pd()
    for i in range (2):
        fd(140)
        left(90)
        fd(60)
        left(90)
    end_fill()
# Random pour la place des portes
    if rdp() == 0 :
        #sépation pour la porte
            fd(15)
            porte()
        #reviens pour la fenetre car porte reset dans le bon sens et se setpour la fenetre
            fd(40)
            pu()
            left(90)
            fd(20)
        #construction de la fenetre
            begin_fill()
            fillcolor('#ffffff')
            pd()
            for i in range(4):
                fd(30)
                right(90)
            end_fill()
        #reset pour f2
            pu()
            bk(20)
            right(90)
            fd(40)
            left(90)
            fd(20)
        #f2
            begin_fill()
            fillcolor('#ffffff')
            pd()
            for i in range(4):
                fd(30)
                rt(90)
            end_fill()
        #reset pour etage
            pu()
            bk(20)
            left(90)
            fd(95)
            right(90)
            fd(60)
            right(90)
    elif rdp() == 1 :
        #sépation pour f1
            pu()
            fd(15)
            left(90)
            fd(20)
        #construction de la f1
            begin_fill()
            fillcolor('#ffffff')
            pd()
            for i in range(4):
                fd(30)
                right(90)
            end_fill()
        #reset pour porte
            pu()
            bk(20)
            right(90)
            fd(40)
        #build of porte
            porte()
        #reviens pour la fenetre car porte reset dans le bon sens et se setpour la fenetre
            fd(40)
            pu()
            left(90)
            fd(20)
        #f2
            begin_fill()
            fillcolor('#ffffff')
            pd()
            for i in range(4):
                fd(30)
                right(90)
            end_fill()
        #reset pour etage
            pu()
            bk(20)
            left(90)
            fd(95)
            right(90)
            fd(60)
            right(90)
    else :
        #sépation pour la porte
            pu()
            fd(15)
            left(90)
            fd(20)
        #construction de la fenetre
            begin_fill()
            fillcolor('#ffffff')
            pd()
            for i in range(4):
                fd(30)
                rt(90)
            end_fill()
        #reset pour f2
            pu()
            right(180)
            fd(20)
            left(90)
            fd(40)
            left(90)
            fd(20)
        #f2
            begin_fill()
            fillcolor('#ffffff')
            pd()
            for i in range(4):
                fd(30)
                rt(90)
            end_fill()
        #reviens pour la porte car fenetre ne reset pas dans le bon sens et se set pour la porte
            pu()
            bk(20)
            right(90)
            fd(40)
            porte()
        #reset pour etage
            pu()
            bk(95)
            left(90)
            fd(60)
            right(90)

def mur(color_b):
    begin_fill()
    fillcolor(color_b)
    pd()
    for i in range(2):
        fd(140)
        left(90)
        fd(60)
        left(90)
    end_fill()
    pu()
    right(90)
    bk(60)
    left(90)

def toit():
    if rd() >= 45 :
        bk(10)
        pd()
        pensize(6)
        fd(160)
        pensize(1)
    else :
        begin_fill()
        fillcolor('black')
        #
        pd()
        bk(16)
        left(30)
        fd(100)
        right(60)
        fd(100)
        left(30)
        bk(150)
        #
        end_fill()
