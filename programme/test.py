#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import font
import time
import random
import os
#import numpy as np
import tkinter as tk
from PIL import Image
from resizeimage import resizeimage
import matplotlib.pyplot as plt
import numpy as np
import pylab

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
int(screen_width)
int(screen_height)
factorW = 0
factorH = 0 
root.destroy()

if screen_width == 1680 and screen_height == 1050 :
    factorW = 1
    factorH = 1
else :
    factorW = (screen_width * 1) / 1680
    factorH = (screen_height * 1) / 1050
    int(factorW)
    int(factorH)


fenetre = Tk()
fenetre.attributes('-fullscreen', 1)
fenDebut = Canvas(fenetre,width=screen_width, height=screen_height, background='black', highlightthickness=0)
fenDebut.place(x="0", y="0")
fontH=font.Font(family='Arial', size=int(23*factorW))
fontB=font.Font(family='Helvetica', size=100)
quitt = font.Font(family='Helvetica', size=500)

livreSave = open("Save.txt", 'r')
hSave = livreSave.read()
livreSave.close()

bil = open("bilan.txt", "r")
bilan = bil.read()
bil.close()
int(bilan)

h="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
h1=h+"         BIENVENUE DANS VOTRE EMPIRE CHER JOUEUR D'EMPIRE ASCENT\n"+h
h2=h+"VOUS IGNOREZ POURQUOI VOUS ETES ICI,CEPENDANT VOUS NE POUVEZ PLUS RECULER...\n"+"IL VA FALLOIR DIRIGER L'UN DES EMPIRES LE PLUS IMPORTANT DE NOTRE HISTOIRE.\n"+"VOUS ALLEZ DEVOIR MELER REFLEXION ET RAPIDITE POUR ESPERER NE PAS SOMBRER ET\n"+"AINSI POUVOIR PROSPERER DANS LE MONDE ENTIER.\n"+h
h3=h+"      LE BUT EST SIMPLE: A CHAQUE REQUETE DE L'UN DE VOS CITOYENS,\n"+"      VOUS DEVREZ EFFECTUER UN CHOIX QUI INFLUENCERA SUR:\n"+"   	- LA RICHESSE DE L'EMPIRE\n"+"   	- LA PUISSANCE MILITAIRE\n"+"   	- LE BONHEUR DE LA POPULATION\n"+"   	- LA PUISSANCE DE LA RELIGION\n"+h
h4=h+"		BONNE CHANCE !\n"+h
h5="ETES VOUS UN HOMME OU UNE FEMME ?"
h6="QUELLE EST VOTRE PSEUDO ?"
h7="VOUS ETES UN HOMME !"
h8="VOUS ETES UNE FEMME !"
h9="﻿EXCELLENT ! VOUS VOILA AUX PORTES DE LA GLOIRE !\n"+"	MAIS QUELLE EST VOTRE PSEUDO?"
h10=h+"EXCELLENT ! VOUS VOILA AUX PORTES DE LA GLOIRE !\n"+"JE VOUS LAISSE MAINTENANT AVEC LE COMMANDANT COUSTEAU.\n"+h
h11=h+"BONJOUR MON EMPEREUR, DES ESCALVES CE SONT REGROUPES SUR \n"+"LA PLACE D'ITALIE, QUE DOIS JE FAIRE ?\n"+"CHOIX 1: 'TUEZ LES TOUS !'\n"+"CHOIX 2: 'LAISSEZ LES POUR UNE FOIS..'\n"+h
h12=h+"		TUEZ LES TOUS !\n"+h
h13=h+"	LAISSEZ LES POUR CETTE FOIS...\n"+h
h14=h+"SEIGNEUR, SEIGNEUR ! MA FERME EST ATTAQUE !\n"+"DES BARBARES VEULENT ENVAHIR L'EMPIRE QUE DEVONS \n"+"	NOUS FAIRE ?\n"+"CHOIX 1: 'ON RIPOSTE !'\n"+"CHOIX 2: 'NE FAITES RIEN, ILS VONT SE CALMER...'\n"+h
h15="ON RIPOSTE !"
h16="	NE FAITES RIEN,ILS VONT SE CALMER"


TAILLE = [466*factorW, 646*factorH]
phot = Image.open('image_principall.png', 'r')
phot = resizeimage.resize_thumbnail(phot, TAILLE)
phot.save('image_principal2.png', phot.format)
photo = PhotoImage(file="image_principal2.png")


TAILLE = [150*factorW, 237*factorH]
phot = Image.open("mouse.png", 'r')
phot = resizeimage.resize_thumbnail(phot, TAILLE)
phot.save('mouse2.png', phot.format)
photoSouris = PhotoImage(file="mouse2.png")

TAILLE = [619*factorW, 491*factorH]

choix=0

fenHistoire = Canvas(fenetre,width=1615*factorW, height=1050*factorH, bg ="black", highlightthickness=0)
fenJoueur = Canvas(fenetre,width=1615*factorW, height=1050*factorH, bg ="black", highlightthickness=0)
fenSouris = Canvas(fenJoueur, width=150, height = 237,bg ="black",  highlightthickness=0)
fenGame = Canvas(fenetre,width=1615*factorW, height=1050*factorH, bg ="black", highlightthickness=0)
fenSouris2 = Canvas(fenGame, width=150, height = 237,bg ="black",  highlightthickness=0)
fenSouris3 = Canvas(fenGame, width=150, height = 237,bg ="black",  highlightthickness=0)
textHomme = Label(fenJoueur, font=fontH, text=h7, fg="white", bg ="black")
textFemme = Label(fenJoueur, font=fontH, text=h8, fg="white", bg ="black")

    
def démarrage():
    boutonDébut=Button(fenDebut, text="COMMENCER", command=sauvegarde, relief=FLAT, height=int(10*factorH), width=int(100*factorW), fg="white", bg ="black", highlightthickness=0, )
    boutonDébut.place(x=int(300*factorW), y=int(700*factorH))
    fenDebut.create_image(500*factorW, 10, anchor=NW, image=photo)
    boutonQuitter=Button(fenDebut, text="QUITTER", command=quitter, relief=FLAT, fg="white", bg ="black", highlightthickness=0,)
    boutonQuitter.place(x=int(1615*factorW), y="0")
    
def sauvegarde():
    if hSave == "true":
        livrejoueur = open("100.txt", 'r')
        global nomJoueur
        nomJoueur = livrejoueur.read()
        livrejoueur.close()
        game10()
    else :
        histoire()

def histoire():
    fenHistoire.place(x="0",y="0")
    fenetre.update()
    textH = Label(fenHistoire, text=h1, font=fontH, fg="white",  bg ="black")
    textH.place(x=int(27*factorW), y="0")
    fenetre.update()
    #time.sleep(5)#
    fenetre.update()
    textH2 = Label(fenHistoire, text=h2, font=fontH, fg="white", bg ="black")
    textH2.place(x=int(27*factorW), y=int(100*factorH))
    fenetre.update()
    #time.sleep(5)#
    fenetre.update()
    textH3 = Label(fenHistoire, text=h3, font=fontH, fg="white", bg ="black")
    textH3.place(x=int(27*factorW), y=int(300*factorH))
    fenetre.update()
    #time.sleep(5)#
    fenetre.update()
    textH4 = Label(fenHistoire, text=h4, font=fontH, fg="white", bg ="black")
    textH4.place(x=int(27*factorW), y=int(600*factorH))
    fenetre.update()
    #time.sleep(5)#
    fenetre.update()
    boutonDemarrer=Button(fenHistoire, text="DÉMARRER", command=ecran, relief=FLAT, height=int(10*factorH), width=int(200*factorW), fg="white", bg ="black", highlightthickness=0,)
    boutonDemarrer.place(x="0", y=int(800*factorH))
    fenetre.update()
    time.sleep(2)#
    fenetre.update()

def ecran():
    fenJoueur.place(x="0",y="0")
    fenSouris.place(x=int(1450*factorW), y=100*factorW)
    fenSouris.create_image(1, 1, anchor=NW, image=photoSouris)
    textH5 = Label(fenJoueur, text=h5, font=fontH, fg="white",  bg ="black")
    textH5.place(x=100*factorW, y=10*factorH)
    textHomme = Label(fenJoueur, font=fontH, text=h7, fg="white", bg ="black")
    textFemme = Label(fenJoueur, font=fontH, text=h8, fg="white", bg ="black")
    fenSouris.bind('<Button-1>',EtreHomme)
    fenSouris.bind('<Button-3>',EtreFemme)
    
def EtreHomme(event):
    textHomme.place(x=int(200*factorW),y=int(80*factorH))
    global sexe
    sexe = "ROI "
    game2()
    
def EtreFemme(event):
    global sexe
    sexe = "REINE "
    textFemme.place(x=int(200*factorW),y=int(80*factorH))
    game2()

def game2():
    fenSouris.destroy()
    fenHistoire.destroy()
    textJoueur = Label(fenJoueur, font=fontH, text=h9, fg="white", bg ="black")
    textJoueur.place(x="0", y=int(160*factorH))
    global entryJoueur
    entryJoueur = Entry(fenJoueur, font=fontH, fg="white", bg ="black")
    entryJoueur.place(x=int(200*factorW), y=(270*factorH))
    global boutonValider
    boutonValider=Button(fenJoueur, text="VALIDER", command=game3, relief=FLAT, height=int(2*factorH), width=int(10*factorW), fg="white", bg ="black", highlightthickness=0)
    boutonValider.place(x=int(550*factorW), y=int(270*factorH))
    
def game3():
    global nomJoueur
    nomJoueur =  entryJoueur.get()
    nomJoueur = nomJoueur.upper()
    entryJoueur.destroy()
    boutonValider.destroy()
    txt1 = Label(fenJoueur, font=fontH, text='PARFAIT ' + nomJoueur +', LE ROYAUME A BESOIN DE VOUS !', fg="white", bg ="black")
    txt1.place(x=30*factorW, y=270*factorH)
    fenetre.update()
    time.sleep(3)#
    fenetre.update()
    game10()
    
def game10():
    fenJoueur.destroy()
    fenGame.place(x="0", y="0")
    fenetre.update()
    global txt2
    txt2 = Label(fenGame, font=fontH, text='Bienvenue dans votre royaume ' + nomJoueur + " !", fg="white", bg ="black")
    txt2.place(x=300*factorW, y=10*factorH)
    fenetre.update()
    time.sleep(2)
    fenetre.update()
    #time.sleep(3)#
    fenetre.update()
    txt2.destroy()
    #txt3.destroy()
    fenetre.update()
    time.sleep(3)#
    fenetre.update()
    global txtH11
    txtH11=Label(fenGame, font=fontH, text=h11, fg='white', bg='black')
    txtH11.place(x=30*factorW, y=10*factorH)
    fenSouris2.place(x=1450*factorW, y=100*factorH)
    fenSouris2.create_image(1, 1, anchor=NW, image=photoSouris)
    fenSouris2.bind('<Button-1>',Choix1)
    fenSouris2.bind('<Button-3>',Choix2)

def Choix1(event):
    fenSouris2.destroy()
    global txtH12
    txtH12=Label(fenGame, font=fontH, text=h12, fg='white', bg='black')
    txtH12.place(x=50*factorW, y=250*factorH)
    fenSouris2.forget()
    bilan1()

def Choix2(event):
    fenSouris2.destroy()
    global txtH13
    txtH13=Label(fenGame, font=fontH, text=h13, fg='white', bg='black')
    txtH13.place(x=50*factorW, y=250*factorH)
    fenSouris2.forget()
    bilan2()

def bilan1():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [3,7,3,5]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(sexe+nomJoueur)
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    phot = Image.open("Bilan.png", 'r')
    phot = resizeimage.resize_thumbnail(phot, TAILLE)
    phot.save('Bilan.png', phot.format)
    global bilanPhoto
    bilanPhoto = PhotoImage(file="Bilan.png")
    fenGame.create_image(1000*factorW, 500*factorH, anchor=NW, image=bilanPhoto)
    fenetre.update()
    time.sleep(6)#
    fenetre.update()
    txtH12.destroy()
    global bilan
    bilan = 1
    game4()

def bilan2():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [5,3,8,5]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(sexe+nomJoueur)
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    phot = Image.open("Bilan.png", 'r')
    phot = resizeimage.resize_thumbnail(phot, TAILLE)
    phot.save('Bilan.png', phot.format)
    global bilanPhoto
    bilanPhoto = PhotoImage(file="Bilan.png")
    fenGame.create_image(1000*factorW, 500*factorH, anchor=NW, image=bilanPhoto)
    fenetre.update()
    time.sleep(6)#
    fenetre.update()
    txtH13.destroy()
    global bilan
    bilan = 2
    game4()

def game4():
    txtH11.destroy()
    global txtH14
    txtH14=Label(fenGame, font=fontH, text=h14, fg='white', bg='black')
    txtH14.place(x=30*factorW, y=10*factorH)
    fenSouris3.place(x=1450*factorW, y=100*factorH)
    fenSouris3.create_image(1, 1, anchor=NW, image=photoSouris)
    fenSouris3.bind('<Button-1>',lambda event : Guerre(choix))
    fenSouris3.bind('<Button-3>',lambda event : Paix(choix))

def Guerre(choix):
    fenSouris3.destroy()
    global txtH15
    txtH15=Label(fenGame, font=fontH, text=h15, fg='white', bg='black')
    txtH15.place(x=100*factorW, y=300*factorH)
    fenetre.update()
    #time.sleep(2)
    fenetre.update()
    if choix:
        bilan3()
    else:
        bilan4()
    
def Paix(choix):
    fenSouris3.destroy()
    global txtH16
    txtH16=Label(fenGame, font=fontH, text=h16, fg='white', bg='black')
    txtH16.place(x=100*factorW, y=300*factorH)
    fenetre.update()
    #time.sleep(2)
    fenetre.update()
    if choix:
        bilan5()
    else:
        bilan6()

def bilan3():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [5,10,0,7]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(sexe+nomJoueur)
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    phot = Image.open("Bilan.png", 'r')
    phot = resizeimage.resize_thumbnail(phot, TAILLE)
    phot.save('Bilan.png', phot.format)
    global bilanPhoto
    bilanPhoto = PhotoImage(file="Bilan.png")
    fenGame.create_image(1000*factorW, 500*factorH, anchor=NW, image=bilanPhoto)
    fenetre.update()
    time.sleep(5)#
    fenetre.update()
    txtH14.destroy()
    txtH15.destroy()
    global bilan
    bilan = 3
    game5()
    
def bilan4():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [7,6,5,7]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(sexe+nomJoueur)
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    phot = Image.open("Bilan.png", 'r')
    phot = resizeimage.resize_thumbnail(phot, TAILLE)
    phot.save('Bilan.png', phot.format)
    global bilanPhoto
    bilanPhoto = PhotoImage(file="Bilan.png")
    fenGame.create_image(1000*factorW, 500*factorH, anchor=NW, image=bilanPhoto)
    fenetre.update()
    time.sleep(5)#
    fenetre.update()
    txtH14.destroy()
    txtH15.destroy()
    global bilan
    bilan = 4
    game5()
    
def bilan5():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [5,4,6,6]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(sexe+nomJoueur)
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    phot = Image.open("Bilan.png", 'r')
    phot = resizeimage.resize_thumbnail(phot, TAILLE)
    phot.save('Bilan.png', phot.format)
    global bilanPhoto
    bilanPhoto = PhotoImage(file="Bilan.png")
    fenGame.create_image(1000*factorW, 500*factorH, anchor=NW, image=bilanPhoto)
    fenetre.update()
    time.sleep(5)#
    fenetre.update()
    txtH14.destroy()
    txtH16.destroy()
    global bilan
    bilan = 5
    game5()
    
def bilan6():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [7,0,10,6]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(sexe+nomJoueur)
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    phot = Image.open("Bilan.png", 'r')
    phot = resizeimage.resize_thumbnail(phot, TAILLE)
    phot.save('Bilan.png', phot.format)
    global bilanPhoto
    bilanPhoto = PhotoImage(file="Bilan.png")
    fenGame.create_image(1000*factorW, 500*factorH, anchor=NW, image=bilanPhoto)
    fenetre.update()
    time.sleep(5)#
    fenetre.update()
    txtH14.destroy()
    txtH16.destroy()
    global bilan
    bilan = 6
    game5()

def game5():
    fenetre.update()
    time.sleep(2)#
    fenetre.update()
    phot.close()
    Quitter=Button(fenGame, text="QUITTER LE JEU",font=fontH, command=quitter,width=50, height=20, relief=FLAT, fg="green", bg ="black", highlightthickness=0)
    Quitter.place(x="0", y="0")
    
def quitter():
    global quitterF
    quitterF = Tk()
    quitterF.attributes('-fullscreen', 1)
    fenquitter = Canvas(quitterF,width=screen_width, height=screen_height, bg ="black", highlightthickness=0)
    fenquitter.place(x="0", y="0")
    txtQuit=Label(fenquitter, font = quitt, text="VOULEZ-VOUS SAUVEGARDER LES DONNEES?", fg='white', bg='black')
    txtQuit.place(x="500", y="0")
    oui=Button(fenquitter, text="OUI",font=fontB, command=sauvegarder,width=50, height=20, relief=FLAT, fg="green", bg ="black", highlightthickness=0)
    oui.place(x="0", y="50")
    non=Button(fenquitter, text="NON", font=fontB, command=fermer,width=50, height=20, relief=FLAT, fg="red", bg ="black", highlightthickness=0)
    non.place(x="500", y="50")
    annuler=Button(fenquitter, text="ANNULER", font=fontB, command=quitterF.destroy,width=50, height=20, relief=FLAT, fg="white", bg ="black", highlightthickness=0)
    annuler.place(x="1000", y="50")

def fermer():
    fig = plt.figure()
    x = [1,2,3,4]
    height = [0,0,0,0]
    width = 0.55
    BarName = ['Religion','Armée','Bonheur','Argent','']
    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=50)
    plt.xlim(0.5)
    plt.ylim(0,10)
    plt.grid()
    plt.ylabel('%')
    plt.title(" ")
    pylab.xticks(x, BarName, rotation=40)
    plt.savefig('Bilan.png')
    Savetxt = open("Save.txt", "w")#
    Savetxt.write("false")#
    Savetxt.close()#
    bil = open("bilan.txt", "w")
    bil.write("0")
    bil.close()
    nomJoueurTxt1 = open("100.txt", "w")
    nomJoueurTxt1.write(" ")
    nomJoueurTxt1.close()
    fenetre.destroy()
    quitterF.destroy()

def sauvegarder():
    nomJoueurTxt1 = open("100.txt", "w")
    nomJoueurTxt1.write(nomJoueur)
    nomJoueurTxt1.close()
    Savetxt = open("Save.txt", "w")#
    Savetxt.write("true")
    bil = open("bilan.txt", "w")
    bil.write(bilan)
    bil.close()
    Savetxt.close()#
    quitterF.destroy()
    fenetre.destroy()
   
démarrage()

fenetre.mainloop()
