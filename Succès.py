
import time
import random
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pylab

#game fonction
def game():
    print ("Succès: Rassurer le paysan")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Seigneur, Seigneur ! Ma ferme est attaqué !")
    print (" Des barbares veulent envahir le empire que devons nous faire ?")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Click Gauche : 'On riposte !'")
    print ("Click Droit : ' Ne faites rien, ils vont se calmer..'")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    widget.bind('<Button-1>',Choix1)
    widget.bind('<Button-3>',Choix2)

def Choix1(event):
    print ("'On riposte !'")
    time.sleep(2)
    print (" Succès débloqué : apprenti empereur")
    
def Choix2(event):
    print ("'Ne faites rien,ils vont se calmer'")
    time.sleep(2)
    print (" Succès débloqué : apprenti empereur")

def Demarrage(event):
    print ("Le jeu va démarrer")
    time.sleep(2)
    game()
    import sys; sys.exit()

while (1) :
    widget = Button(None, text='Démarrer Empire Ascent')
    widget.pack()
    widget.bind('<Button-1>',Demarrage)
    widget.mainloop()
