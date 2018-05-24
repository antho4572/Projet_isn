
import time
import random
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pylab

#game fonction3
def game3():
    print ("Général De gaulle :") 
    print ("Il y a des bandits dans les régions montagneuses du Sud !")
    print ("Click Gauche: 'Je m'en fiche !'")
    print ("Click Droit: 'Envoyer l'officier Jean Dumoulin pour diriger la région' ")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    widget.bind('<Button-1>',Choix1)
    widget.bind('<Button-3>',Choix2)

def Choix1(event):
    print ("'Je m'en fiche !'")
    time.sleep(2)
    print ("Général De gaulle :")
    print ("La région est maintenant corompue et dangereuse")
    print ("Click Gauche: 'Envoyer l'armée !'")
    print ("Click Droit: 'Donnez leur ce qu'ils veulent'")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    widget.bind('<Button-1>',Choix3)
    widget.bind('<Button-3>',Choix4)
    
def Choix2(event):
    print ("'Envoyer l'officier Jean Dumoulin pour diriger la région'")
    time.sleep(2)
    print ("Jean Dumoulin :")
    print ("C'est un honneur, je ferais de mon mieux...")
    print ("Click Gauche: 'Soyez juste'")
    print ("Click Droit: 'Soyez dur'")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    widget.bind('<Button-1>',Choix5)
    widget.bind('<Button-3>',Choix6)

def Choix3(event):
    print ("'Envoyer l'armée !'")
    time.sleep(2)
def Choix4(event):
    print ("'Donnez leur ce qu'ils veulent'")
    time.sleep(2)

def Choix5(event):
    print ("'Soyez juste'")
    time.sleep(2)
def Choix6(event):
    print ("'Soyez dur'")
    time.sleep(2)    

def Demarrage(event):
    print ("Le jeu va démarrer")
    time.sleep(2)
    game3()
    import sys; sys.exit()

while (1) :
    widget = Button(None, text='Démarrer Empire Ascent')
    widget.pack()
    widget.bind('<Button-1>',Demarrage)
    widget.mainloop()

