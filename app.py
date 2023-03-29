from matplotlib.colors import LightSource  #modules pour ajuster l'éclairage et les couleurs mais pas entièrement
from matplotlib.colors import Normalize  # soit des ombres bleus, soit rouges, bizarre...
from tkinter import *
import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import os
import numpy

pygame.init()

####### Initialisation des variables #######

taille = 0
c = 0
points = 1

# Palette de couleurs
Eau_Abyss = pygame.Color("#2b42d6")
Eau_Profonde_1 = pygame.Color("#2f55eb")
Eau_Profonde_2 = pygame.Color("#376efa")
Eau_Pied = pygame.Color("#4185fa")
Eau_Surface = pygame.Color("#4c94ff")
Eau_Bord = pygame.Color("#57a3ff")
Sable_Bas = pygame.Color("#ffff00")
Sable_Moyen = pygame.Color("#ffff7a")
Foret_0 = pygame.Color("#62d64d")
Foret_1 = pygame.Color("#46bd31")
Foret_2 = pygame.Color("#36ad23")
Foret_Rousse_1 = pygame.Color("#b85f11")
Foret_Rousse_2 = pygame.Color("#b83d11")
Neige_0 = pygame.Color("#e5f9ff")
Neige_1 = pygame.Color("#ebffff")
Neige_2 = pygame.Color("#ffffff")
Neige_2_Correctif = pygame.Color("#ffffff")

listeCouleur = [Eau_Abyss, Eau_Profonde_1, Eau_Profonde_2, Eau_Pied, Eau_Surface, Eau_Bord, Sable_Bas, Sable_Moyen,
                Foret_0, Foret_1, Foret_2, Foret_Rousse_1, Foret_Rousse_2, Neige_0, Neige_1, Neige_2, Neige_2_Correctif]

####### Méthode pour centrer les fenêtres #######

####### Paramètres de la fenêtre principale #######

os.environ['SDL_VIDEO_CENTERED'] = "%d,%d"  # centrer la fenêtre

# créer une première fenêtre
window = Tk()

# personnaliser cette fenêtre
window.title("F & S")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("mountain.ico")
window.config(background='#4065A4')

# créer la frame
frame = Frame(window, bg='#4065A4')

# initialiser les variables
running = True
screenDeBase = False


########################################################################################################################

####### Méthode pour le menu principal #######


def MainMenu():
    frame.destroy()
    MainMenu = Toplevel(window)
    MainMenu.geometry("720x480")
    MainMenu.config(background='#4065A4')
    window.withdraw()
    MainMenu.iconbitmap("mountain.ico")

    ####### Ajout du titre #######

    label_title = Label(MainMenu, text='\nFractals & Survie', font=("Impact", 25), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'un sous-titre #######

    label_subtitle = Label(MainMenu, text="Sélectionnez un mode\n", font=("Impact", 18), bg='#4065A4', fg='white')
    label_subtitle.pack()

    ####### Ajout du premier bouton #######

    premierB = Button(MainMenu, text="> Nouvelle Surface", font=("Impact", 12), bg='#4065A4', fg='white',
                      command=premierMode)
    premierB.pack(pady=5, fill=Y)
    premierB.click = False

    ####### Ajout du deuxième bouton #######

    deuxiemeB = Button(MainMenu, text="> Carte", font=("Impact", 12), bg='#4065A4', fg='white', command=deuxiemeMode)
    deuxiemeB.pack(pady=5, fill=Y)
    deuxiemeB.click = False

    ####### Ajout du troisième bouton #######

    troisiemeB = Button(MainMenu, text="> Vue en strates", font=("Impact", 12), bg='#4065A4', fg='white',
                        command=troisiemeMode)
    troisiemeB.pack(pady=5, fill=Y)
    troisiemeB.click = False

    ####### Ajout du quatrième bouton #######

    quatriemeB = Button(MainMenu, text="> Vue en ombres", font=("Impact", 12), bg='#4065A4', fg='white',
                        command=quatriemeMode)
    quatriemeB.pack(pady=5, fill=Y)
    quatriemeB.click = False

    ####### Ajout du cinquième bouton #######

    cinquiemeB = Button(MainMenu, text="> Vue en fil de fer", font=("Impact", 12), bg='#4065A4', fg='white',
                        command=cinquiemeMode)
    cinquiemeB.pack(pady=5, fill=Y)
    cinquiemeB.click = False

    ####### Ajout du sixième bouton #######

    sixiemeB = Button(MainMenu, text="> Le jeu", font=("Impact", 12), bg='#4065A4', fg='white', command=sixiemeMode)
    sixiemeB.pack(pady=5, fill=Y)
    sixiemeB.click = False

    ####### Création d'une barre de menu #######

    menu_bar = Menu(MainMenu)

    ####### Création d'un premier menu #######

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Quitter", command=MainMenu.quit)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)

    ####### Configuration de la fenêtre pour ajouter la menu bar #######

    MainMenu.config(menu=menu_bar)


########################################################################################################################

####### Méthode pour le premier mode #######


def premierMode():
    # personnaliser cette fenêtre
    premierMode = Toplevel(window)
    premierMode.geometry("720x480")
    premierMode.config(background='#4065A4')
    window.withdraw()
    premierMode.iconbitmap("mountain.ico")

    ####### Pour récupérer les données #######

    def pri():
        maille = -1

        while maille < 0 or maille > 3:
            maille = int(password_1.get())

        pas = 2 ** (7 - maille)  ##pas = 2 puissance (7-maille)

        hauteurBase = int(password_2.get())
        deviation = int(password_3.get())
        graine = int(password_4.get())
        taille = int(password_5.get())

        random.seed(graine)
        graineTransformee = random.randint(0, 100000000000)  # générer un nombre aléatoire qui varie selon la graine
        print(graineTransformee)

        listeHauteur = numpy.zeros((taille + 1, taille + 1))  # tableau de taille par taille

        n = hauteurBase / 16

        fichierSauvegarderN = open("data/save_n.txt", "w")
        print("N : ", n)
        nPourFichier = str(n)
        fichierSauvegarderN.write(nPourFichier)
        fichierSauvegarderN.close()

        ####### Lancement de la boucle principale #######

        pygame.init()

        surface = True  # boucle principale de pygame
        x = 0
        y = 0
        lancerSurfaceDeBase = True
        lancerCalculFractal = True
        q = 0
        e = 0

        ecran = pygame.display.set_mode((taille, taille))  # définir la taille de la fenêtre
        pygame.display.set_caption("Votre nouvelle carte")  # titrer la fenêtre
        ecran.fill((0, 0, 0))  # fenêtre noire

        pygame.display.flip()  # actualisation de la fenêtre

        while surface:

            for event in pygame.event.get():  # cliquer sur la croix, ou appuyer sur echap pour fermer
                if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == QUIT):
                    surface = False

                if event.type == KEYDOWN and event.key == K_RETURN:
                    surface = False

            if lancerSurfaceDeBase == True:
                for x in range(0, taille, pas):
                    for y in range(0, taille, pas):
                        rnd = (random.randint(0, 100) / 100)
                        listeHauteur[x][y] = rnd * hauteurBase

                        if listeHauteur[x][y] < n:
                            listeHauteur[x][y] = n

                        c = round(listeHauteur[x][y] / n)

                        if c > 16:
                            c = 16
                        x = int(x)
                        y = int(y)
                        c = int(c)
                        pygame.draw.rect(ecran, listeCouleur[c], [x, y, 1, 1])
                lancerSurfaceDeBase = False

            ####### Calcul fractal #######

            if lancerCalculFractal:

                while pas > 1:
                    q = int(pas / 2)
                    e = int(deviation / 2)

                    x = int(x)  # pour les entiers qui sont devenus floats
                    y = int(y)  # à cause d'une divisions ou autre
                    taille = int(taille)  # pour qu'ils restent des entiers et que le
                    pas = int(pas)  # programme ne les considère pas comme des floats

                    for x in range(q, taille - q, pas):
                        for y in range(q, taille - q, pas):  # Correction on ne commence pas à 0 mais à q
                            hauteurBase = int((listeHauteur[x - q][y - q] + listeHauteur[x - q][y + q] +
                                               listeHauteur[x + q][y - q] + listeHauteur[x + q][
                                                   y + q]) / 4 + deviation * (random.randint(0, 100) / 100) - e)

                            if hauteurBase < n:
                                hauteurBase = int(n)

                            c = int(hauteurBase / n)
                            if c > 16:
                                c = 16
                            c = round(c)
                            listeHauteur[x][y] = int(hauteurBase)

                            pygame.draw.rect(ecran, listeCouleur[c], [x, y, 1, 1])

                    for x in range(pas, taille - pas, pas):
                        for y in range(q, taille - q, pas):  # Correction on ne commence pas à 0 mais à q
                            hauteurBase = int((listeHauteur[x - q][y] + listeHauteur[x + q][y] + listeHauteur[x][
                                y - q] + listeHauteur[x][y + q]) / 4 + deviation * (random.randint(0, 100) / 100) - e)

                            if hauteurBase < n:
                                hauteurBase = int(n)

                            c = int(hauteurBase / n)
                            if c > 16:
                                c = 16
                            c = round(c)
                            listeHauteur[x][y] = int(hauteurBase)
                            pygame.draw.rect(ecran, listeCouleur[c], [x, y, 1, 1])

                            hauteurBase = int((listeHauteur[y - q][x] + listeHauteur[y + q][x] + listeHauteur[y][
                                x - q] + listeHauteur[y][x + q]) / 4 + deviation * (random.randint(0, 100) / 100) - e)

                            if hauteurBase < n:
                                hauteurBase = int(n)

                            c = int(hauteurBase / n)
                            if c > 16:
                                c = 16
                            c = round(c)
                            listeHauteur[y][x] = int(hauteurBase)

                            pygame.draw.rect(ecran, listeCouleur[c], [x, y, 1, 1])

                    i = int(q)
                    for i in range(q, taille - q, pas):
                        hauteurBase = int(
                            (listeHauteur[0][i - q] + listeHauteur[0][i + q] + listeHauteur[q][i]) / 3 + deviation * (
                                    random.randint(0, 100) / 100) - e)

                        if hauteurBase < n:
                            hauteurBase = int(n)

                        listeHauteur[0][i] = int(hauteurBase)

                        hauteurBase = int((listeHauteur[taille][i - q] + listeHauteur[taille][i + q] +
                                           listeHauteur[taille - q][i]) / 3 + deviation * (
                                                  random.randint(0, 100) / 100) - e)
                        if hauteurBase < n:
                            hauteurBase = int(n)

                        listeHauteur[taille][i] = hauteurBase  # ********

                        hauteurBase = int(
                            (listeHauteur[i - q][0] + listeHauteur[i + q][0] + listeHauteur[i][q]) / 3 + deviation * (
                                    random.randint(0, 100) / 100) - e)

                        if hauteurBase < n:
                            hauteurBase = int(n)

                        listeHauteur[i][0] = int(hauteurBase)  # 630

                        hauteurBase = int((listeHauteur[i - q][taille] + listeHauteur[i + q][taille] + listeHauteur[i][
                            taille - q]) / 3 + deviation * (random.randint(0, 100) / 100) - e)  # 640
                        if hauteurBase < n:
                            hauteurBase = int(n)

                        listeHauteur[i][taille] = int(hauteurBase)

                    pas = pas / 2
                    deviation = deviation / 2
                lancerCalculFractal = False

                fichierSauvegarderHauteur = open("data/save_hauteur.txt", "w")
                fichierSauvegarderTaille = open("data/save_taille.txt", "w")

                for x in range(0, taille):
                    for y in range(0, taille):
                        hauteurBase = int(listeHauteur[x][y])

                        hauteurBasePourFichier = str(hauteurBase)

                        # fichierSauvegarderHauteur.write(hauteurBasePourFichier+'\ni')
                        fichierSauvegarderHauteur.write(hauteurBasePourFichier + '\n')

                        if hauteurBase < n:
                            hauteurBase = int(n)

                        c = int(hauteurBase / n)

                        if c > 16:
                            c = 16
                        c = round(c)
                        pygame.draw.rect(ecran, listeCouleur[c], [x, y, 1, 1])

                taillePourFichier = str(taille)
                fichierSauvegarderTaille.write(taillePourFichier)
                fichierSauvegarderHauteur.close()
                fichierSauvegarderTaille.close()
                pygame.display.flip()  # actualisation de la fenêtre
                pygame.image.save(ecran, "carte.png")
        pygame.quit()

    # créer la frame
    frame = Frame(premierMode, bg='#4065A4')

    ####### Ajout d'une image #######

    # création d'image
    width = 300
    height = 300
    image = PhotoImage(file='fir.png').zoom(35).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
    canvas.create_image(width / 2, height / 2, image=image)
    canvas.grid(row=0, column=0, sticky=W)

    ####### Création d'une sous-boîte #######

    right_frame = Frame(frame, bg='#4065A4')

    ####### Ajout d'un titre #######

    label_title = Label(right_frame, text="Choisissez une maille (0-3)", font=("Impact", 14), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'un champ #######

    password_1 = Entry(right_frame, font=("Impact", 14), bg='#4065A4', fg='white')
    password_1.pack()

    ####### Ajout d'un titre #######

    label_title = Label(right_frame, text="Choisissez une hauteur de base", font=("Impact", 14), bg='#4065A4',
                        fg='white')
    label_title.pack()

    ####### Ajout d'un champ #######

    password_2 = Entry(right_frame, font=("Impact", 14), bg='#4065A4', fg='white')
    password_2.pack()

    ####### Ajout d'un titre #######

    label_title = Label(right_frame, text="Choisissez une déviation", font=("Impact", 14), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'un champ #######

    password_3 = Entry(right_frame, font=("Impact", 14), bg='#4065A4', fg='white')
    password_3.pack()

    ####### Ajout d'un titre #######

    label_title = Label(right_frame, text="Choisissez une graine de génération", font=("Impact", 14), bg='#4065A4',
                        fg='white')
    label_title.pack()

    ####### Ajout d'un champ #######

    password_4 = Entry(right_frame, font=("Impact", 14), bg='#4065A4', fg='white')
    password_4.pack()

    ####### Ajout d'un titre #######

    label_title = Label(right_frame, text="Choisissez une taille\n (512, 256, 128, 64, 32 ou 1024)",
                        font=("Impact", 14), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'un champ #######

    password_5 = Entry(right_frame, font=("Impact", 14), bg='#4065A4', fg='white')
    password_5.pack()

    ####### Ajout d'un bouton #######

    generer = Button(right_frame, text="Générer", font=("Impact", 15), bg='#4065A4', fg='white', command=pri)
    generer.pack(pady=5, fill=X)

    ####### Placement de la sous-boîte à droite de la frame principale #######
    right_frame.grid(row=0, column=1, sticky=W)

    # ajouter
    frame.pack(expand=YES)

    # afficher
    window.mainloop()


########################################################################################################################

####### Méthode pour le deuxième mode #######


def deuxiemeMode():
    # personnaliser cette fenêtre
    deuxiemeMode = Toplevel(window)
    deuxiemeMode.geometry("720x480")
    deuxiemeMode.config(background='#4065A4')
    window.withdraw()
    deuxiemeMode.iconbitmap("mountain.ico")

    ####### Ajout d'un try catch au cas où le fichier ne serait pas ouvrable #######

    try:
        open("data/save_hauteur.txt", "r")  # s'il y'a un fichier, l'ouvrir
    except IOError:
        print("Le fichier n'a pas pu être ouvert")  # s'il n'y a pas de fichier, quitter

    ####### Ajout d'un titre #######

    label_title = Label(deuxiemeMode, text='\nLa carte actuelle', font=("Impact", 25), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'une image #######

    # création d'une image
    width = 350
    height = 350
    image = PhotoImage(file='carte.png').zoom(45).subsample(32)
    canvas = Canvas(deuxiemeMode, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
    canvas.create_image(width / 2, height / 2, image=image)
    canvas.pack()

    # afficher
    deuxiemeMode.mainloop()


########################################################################################################################

####### Méthode pour le troisième mode #######


def troisiemeMode():

    ####### Ajout d'un try catch au cas où le fichier ne serait pas ouvrable #######

    try:
        fichierH = open("data/save_hauteur.txt", "r")  # s'il y'a un fichier, l'ouvrir
    except IOError:
        print("Le fichier n'a pas pu être ouvert")  # s'il n'y a pas de fichier, quitter

    fichierT = open("data/save_taille.txt", "r")
    tailleStr = fichierT.read()
    taille = int(tailleStr)
    fichierT.close()

    fichierN = open("data/save_n.txt", "r")
    nStr = fichierN.read()
    n = float(nStr)
    fichierN.close()

    # personnaliser cette fenêtre
    troisiemeMode = Toplevel(window)
    troisiemeMode.geometry("720x480")
    troisiemeMode.config(background='#4065A4')
    window.withdraw()
    troisiemeMode.iconbitmap("mountain.ico")

    ####### Pour récupérer les données #######

    def strates():
        modeStrate = -1

        while modeStrate < 0 or modeStrate > 3:
            modeStrate = int(password_1.get())

        ####### 1 #######

        if modeStrate == 1:

            def mesh():

                points = -1

                while points < 0 or points > 4:
                    points = int(password.get())

                    numlinefile = 0

                    positionX = []
                    positionY = []
                    positionZ = []
                    couleurC = []

                    x = range(0, taille)
                    y = range(0, taille)
                    X, Y = numpy.meshgrid(x, y)
                    Z = numpy.zeros((taille, taille))

                    listeHauteur = numpy.zeros((taille + 1, taille + 1))

                    lines = fichierH.readlines()  # Récupérer les données du fichier
                    for x in range(0, taille):
                        for y in range(0, taille):
                            listeHauteur[x][y] = int(lines[numlinefile])
                            numlinefile = numlinefile + 1
                    fichierH.close()

                    for x in range(0, taille, points):
                        for y in range(0, taille, points):

                            hauteurBase = int(listeHauteur[x][y])
                            if hauteurBase < n:
                                hauteurBase = int(n)

                            c = int(hauteurBase / n)
                            if c > 16:
                                c = 16
                            c = round(c)

                            positionX.append(x)
                            positionY.append(y)
                            positionZ.append(hauteurBase)
                            couleurC.append(c)

                    dataX = numpy.array(positionX)
                    dataY = numpy.array(positionY)
                    Z[dataX, dataY] = positionZ

                    fig = plt.figure(num='Terrain en 3D en polygones')
                    ax = fig.add_subplot(111, projection='3d')
                    ax._axis3don = False
                    fig.patch.set_facecolor('#cccccc')
                    ax.set_facecolor('#dddddd')

                    ax.plot_surface(X, Y, Z, cmap=cm.gist_earth, linewidth=0,
                                    antialiased=False)  # antialisased = ajouter des lignes blanches entre les meshs
                    plt.show()  # d'autres cmap (sous la forme cm.couleur) : https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html?highlight=colormap

            suite = Toplevel(window)
            suite.geometry("720x480")
            suite.config(background='#4065A4')
            window.withdraw()
            suite.iconbitmap("mountain.ico")

            ####### Ajout d'un titre #######

            label_title = Label(suite, text="Pourcentage de pics :\n 4=25% - 3=33% - 2=50% - 1=100%",
                                font=("Impact", 14), bg='#4065A4', fg='white')
            label_title.pack()

            ####### Ajout d'un champ #######

            password = Entry(suite, font=("Impact", 14), bg='#4065A4', fg='white')
            password.pack()

            ####### Ajout d'un bouton #######

            generer = Button(suite, text="Générer", font=("Impact", 15), bg='#4065A4', fg='white', command=mesh)
            generer.pack(pady=5)

            ####### Ajout d'une image #######

            # création d'image
            width = 300
            height = 300
            image = PhotoImage(file='trees.png').zoom(35).subsample(32)
            canvas = Canvas(suite, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
            canvas.create_image(width / 2, height / 2, image=image)
            canvas.pack()

            # ajouter
            suite.pack(expand=YES)

        ####### 2 #######

        if modeStrate == 2:

            def points():

                points = -1

                while points < 0 or points > 4:
                    points = int(password.get())

                    numlinefile = 0

                    fig = plt.figure(num='Terrain en 3D en points')
                    ax = fig.add_subplot(111, projection='3d')
                    ax._axis3don = False
                    fig.patch.set_facecolor('#000000')
                    ax.set_facecolor('#111111')

                    positionX = []
                    positionY = []
                    positionZ = []
                    couleurC = []

                    listeHauteur = numpy.zeros((taille + 1, taille + 1))

                    lines = fichierH.readlines()  # Récupérer les données du fichier
                    for x in range(0, taille):
                        for y in range(0, taille):
                            listeHauteur[x][y] = int(lines[numlinefile])
                            numlinefile = numlinefile + 1
                    fichierH.close()

                    for x in range(0, taille, points):
                        for y in range(0, taille, points):

                            hauteurBase = int(listeHauteur[x][y])
                            if hauteurBase < n:
                                hauteurBase = int(n)

                            c = int(hauteurBase / n)
                            if c > 16:
                                c = 16
                            c = round(c)

                            positionX.append(x)
                            positionY.append(y)
                            positionZ.append(hauteurBase)
                            couleurC.append(c)

                    ax.scatter(positionX, positionY, positionZ, c=couleurC, marker='o')

                    plt.show()

            suite = Toplevel(window)
            suite.geometry("720x480")
            suite.config(background='#4065A4')
            window.withdraw()
            suite.iconbitmap("mountain.ico")

            ####### Ajout d'un titre #######

            label_title = Label(suite, text="Pourcentage de points :\n 4=25%  -  3=33%  -  2=50%  -  1=100% (lourd !)",
                                font=("Impact", 14), bg='#4065A4', fg='white')
            label_title.pack()

            ####### Ajout d'un champ #######

            password = Entry(suite, font=("Impact", 14), bg='#4065A4', fg='white')
            password.pack()

            ####### Ajout d'un bouton #######

            generer = Button(suite, text="Générer", font=("Impact", 15), bg='#4065A4', fg='white', command=points)
            generer.pack(pady=5)

            ####### Ajout d'une image #######

            # création d'image
            width = 300
            height = 300
            image = PhotoImage(file='trees.png').zoom(35).subsample(32)
            canvas = Canvas(suite, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
            canvas.create_image(width / 2, height / 2, image=image)
            canvas.pack()

            # ajouter
            suite.pack(expand=YES)

        ####### 3 #######

        if modeStrate == 3:
            suite = Toplevel(window)
            suite.geometry("720x480")
            suite.config(background='#4065A4')
            window.withdraw()
            suite.iconbitmap("mountain.ico")

            ####### Ajout d'un titre #######

            label_title = Label(suite, text="Fractals & Survie", font=("Impact", 40), bg='#4065A4', fg='white')
            label_title.pack()

            ####### Ajout d'un premier sous-titre #######

            label_subtitle_1 = Label(suite, text="Le jeu d'aventure d'un autre temps", font=("Impact", 25),
                                     bg='#4065A4', fg='white')
            label_subtitle_1.pack(pady=0.5, fill=Y)

            ####### Ajout d'un deuxième sous-titre #######

            label_subtitle_2 = Label(suite, text="Ce mode de jeu n'est pas encore disponible",
                                     font=("Impact", 18),
                                     bg='#4065A4', fg='white')
            label_subtitle_2.pack(pady=100, fill=Y)

########################################################################################################################

    # créer la frame
    frame = Frame(troisiemeMode, bg='#4065A4')

    ####### Ajout d'une image #######

    # création d'image
    width = 300
    height = 300
    image = PhotoImage(file='fir.png').zoom(35).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
    canvas.create_image(width / 2, height / 2, image=image)
    canvas.grid(row=0, column=0, sticky=W)

    ####### Création d'une sous-boîte #######

    right_frame = Frame(frame, bg='#4065A4')

    ####### Ajout d'un titre #######

    label_title = Label(right_frame, text="Mode de strates :\n\n 1 -Meshs[3D]\n  2 -Points[3D]\n  3 -Pixels[2D]\n", font=("Impact", 14), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'un champ #######

    password_1 = Entry(right_frame, font=("Impact", 14), bg='#4065A4', fg='white')
    password_1.pack()

    ####### Ajout d'un bouton #######

    generer = Button(right_frame, text="Continuer", font=("Impact", 15), bg='#4065A4', fg='white', command=strates)
    generer.pack(pady=5, fill=X)

    ####### Placement de la sous-boîte à droite de la frame principale #######
    right_frame.grid(row=0, column=1, sticky=W)

    # ajouter
    frame.pack(expand=YES)

    # afficher
    window.mainloop()

########################################################################################################################

####### Méthode pour le quatrième mode #######


def quatriemeMode():
    from matplotlib.colors import LightSource  # modules pour ajuster l'éclairage et les couleurs, pas totalement
    from matplotlib.colors import \
        Normalize  # soit des ombres bleus, soit rouges, bizarre...

    try:
        fichierH = open("data/save_hauteur.txt", "r")  # s'il y'a un fichier, l'ouvrir
        lancerBoucle = True
    except IOError:
        print("Le fichier n'a pas pu être ouvert")  # s'il n'y a pas de fichier, quitter
        lancerBoucle = False

    if lancerBoucle == True:
        fichierT = open("data/save_taille.txt", "r")
        tailleStr = fichierT.read()
        taille = int(tailleStr)
        fichierT.close()

        fichierN = open("data/save_n.txt", "r")
        nStr = fichierN.read()
        n = float(nStr)
        fichierN.close()

    ####### LANCEMENT #######

    numlinefile = 0

    positionX = []
    positionY = []
    positionZ = []
    couleurC = []

    x = range(0, taille)
    y = range(0, taille)
    X, Y = numpy.meshgrid(x, y)
    Z = numpy.zeros((taille, taille))

    listeHauteur = numpy.zeros((taille + 1, taille + 1))

    lines = fichierH.readlines()  # on récupère les données du fichier
    for x in range(0, taille):
        for y in range(0, taille):
            listeHauteur[x][y] = int(lines[numlinefile])
            numlinefile = numlinefile + 1
        fichierH.close()

    for x in range(0, taille, points):
        for y in range(0, taille, points):

            hauteurBase = int(listeHauteur[x][y])
            if hauteurBase < n:
                hauteurBase = int(n)

            c = int(hauteurBase / n)
            if c > 16:
                c = 16
            c = round(c)

            positionX.append(x)
            positionY.append(y)
            positionZ.append(hauteurBase)
            couleurC.append(c)

    dataX = numpy.array(positionX)
    dataY = numpy.array(positionY)
    Z[dataX, dataY] = positionZ

    fig = plt.figure(num='Terrain en 3D en polygones')
    ax = fig.add_subplot(111, projection='3d')
    ax._axis3don = False
    fig.patch.set_facecolor('#cccccc')
    ax.set_facecolor('#dddddd')

    norm = Normalize(vmin=0, vmax=0)
    ls = LightSource(azdeg=5, altdeg=5)
    rgb = ls.shade(Z, plt.cm.jet, norm=norm)  # -----------------BLEU

    ax.plot_surface(X, Y, Z, cmap=cm.gist_earth, linewidth=0, antialiased=False,
                    facecolors=rgb)  # antialisased = ajout de lignes blanches entre les meshs
    # d'autres cmap (sous la forme cm.couleur) : https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html?highlight=colormap
    plt.show()

    try:
        fichierH = open("data/save_hauteur.txt", "r")  # s'il y'a un fichier, l'ouvrir
        lancerBoucle = True
    except IOError:
        print("Le fichier n'a pas pu être ouvert")  # s'il n'y a pas de fichier, quitter
        lancerBoucle = False

    if lancerBoucle == True:
        fichierT = open("data/save_taille.txt", "r")
        tailleStr = fichierT.read()
        taille = int(tailleStr)
        fichierT.close()

        fichierN = open("data/save_n.txt", "r")
        nStr = fichierN.read()
        n = float(nStr)
        fichierN.close()

    numlinefile = 0

    x = range(0, taille)
    y = range(0, taille)

    listeHauteur = numpy.zeros((taille + 1, taille + 1))

    lines = fichierH.readlines()  # on récupère les données du fichier
    for x in range(0, taille):
        for y in range(0, taille):
            listeHauteur[x][y] = int(lines[numlinefile])
            numlinefile = numlinefile + 1
    fichierH.close()

########################################################################################################################

####### Méthode pour le cinquième mode #######


def cinquiemeMode():
    try:
        fichierH = open("data/save_hauteur.txt", "r")  # s'il y'a un fichier, l'ouvrir
        lancerBoucle = True
    except IOError:
        print("Le fichier n'a pas pu être ouvert")  # s'il n'y a pas de fichier, quitter
        lancerBoucle = False

    if lancerBoucle == True:
        fichierT = open("data/save_taille.txt", "r")
        tailleStr = fichierT.read()
        taille = int(tailleStr)
        fichierT.close()

        fichierN = open("data/save_n.txt", "r")
        nStr = fichierN.read()
        n = float(nStr)
        fichierN.close()

    numlinefile = 0

    x = range(0, taille)
    y = range(0, taille)

    listeHauteur = numpy.zeros((taille + 1, taille + 1))

    lines = fichierH.readlines()  # on récupère les données du fichier
    for x in range(0, taille):
        for y in range(0, taille):
            listeHauteur[x][y] = int(lines[numlinefile])
            numlinefile = numlinefile + 1
    fichierH.close()

    filDeFer = True  # boucle principale de pygame

    lancerFilDeFerDeBase = True
    o = 160
    k = 0

    ecran = pygame.display.set_mode((800, 600))  # définir la taille de la fenêtre
    pygame.display.set_caption("Génération de la map en fil de fer")  # titrer la fenêtre
    ecran.fill((0, 0, 0))  # fenêtre noire

    pygame.draw.line(ecran, (127, 0, 127), [+30, +150], [320+30, 0+150], 1)
    pygame.draw.line(ecran, (127, 0, 127), [320+30, 0+150], [640+30, 40+150], 1)

    pygame.display.flip()  # actualisation de la fenêtre

    tableauC = numpy.zeros(320)
    for tableauCParcours in range(0, 320): # initialiser toutes les cases du tableau à 10
        tableauC[tableauCParcours] = 10

    while filDeFer == True:

        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == QUIT):  # bouton quitter fonctionnel
                pygame.quit()
                sys.exit()

            for y in range(0, 128, 2):

                for event in pygame.event.get():  # cliquer sur la croix, ou appuyer sur echap pour fermer
                    if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == QUIT):
                        carte = False

                positionXCrayon = (o * 4) - 320 + 30
                positionYCrayon = tableauC[o + k] + 150
                k = 0
                o = 160 - y
                if o < 0:
                    k = -o
                for x in range(k, 128, 2):
                    t = listeHauteur[x][y] + y + x
                    uneAutreHauteur = max(tableauC[x + o], t)
                    tableauC[x + o] = uneAutreHauteur
                    pygame.draw.line(ecran, (127, 0, 127), [positionXCrayon, positionYCrayon],
                                 [(o + x) * 4 - 320 + 30, uneAutreHauteur + 150], 1)
                    positionXCrayon = (o + x) * 4 - 320 + 30
                    positionYCrayon = uneAutreHauteur + 150

            pygame.draw.line(ecran, (127, 0, 127), [positionXCrayon, positionYCrayon], [(o + x) * 4 - 322 + 30, uneAutreHauteur + 150], 1)
            pygame.display.flip()  # actualisation de la fenêtre


########################################################################################################################

####### Méthode pour le sixième mode #######


def sixiemeMode():
    sixiemeMode = Toplevel(window)
    sixiemeMode.geometry("720x480")
    sixiemeMode.config(background='#4065A4')
    window.withdraw()
    sixiemeMode.iconbitmap("mountain.ico")

    ####### Ajout d'un titre #######

    label_title = Label(sixiemeMode, text="Fractals & Survie", font=("Impact", 40), bg='#4065A4', fg='white')
    label_title.pack()

    ####### Ajout d'un premier sous-titre #######

    label_subtitle_1 = Label(sixiemeMode, text="Le jeu d'aventure d'un autre temps", font=("Impact", 25),
                             bg='#4065A4', fg='white')
    label_subtitle_1.pack(pady=0.5, fill=Y)

    ####### Ajout d'un deuxième sous-titre #######

    label_subtitle_2 = Label(sixiemeMode, text="Ce mode de jeu n'est pas encore disponible", font=("Impact", 18),
                             bg='#4065A4', fg='white')
    label_subtitle_2.pack(pady=100, fill=Y)


########################################################################################################################

####### Méthode pour le clique sur le bouton #######


def valider():
    if not commencer.click:
        commencer.click = True


########################################################################################################################

####### Tant que le programme fonctionne, il s'affiche l'intérieur de la boucle #######


while running:

    ####### Ajout d'un titre #######

    label_title = Label(frame, text="Fractals & Survie", font=("Impact", 40), bg='#4065A4', fg='white')
    label_title.pack(expand=YES)

    ####### Ajout d'un sous-titre #######

    label_subtitle = Label(frame, text="Le jeu d'aventure d'un autre temps", font=("Impact", 25), bg='#4065A4',
                           fg='white')
    label_subtitle.pack(expand=YES)

    ####### Ajout d'un bouton #######

    commencer = Button(frame, text="Commencez le jeu", font=("Impact", 25), bg='#4065A4', fg='white', command=MainMenu)
    commencer.pack(pady=25, fill=X)
    commencer.click = False

    ####### Ajout d'une image #######

    # création d'image
    width = 90
    height = 90
    image = PhotoImage(file='fire.png').zoom(35).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
    canvas.create_image(width / 2, height / 2, image=image)
    canvas.pack()

    # ajouter
    frame.pack(expand=YES)

    ####### Création d'une barre de menu #######

    menu_bar = Menu(window)

    ####### Création d'un premier menu #######

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Quitter", command=window.quit)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)

    ####### Configuration de la fenêtre pour ajouter la menu bar #######

    window.config(menu=menu_bar)

    ####### Si l'évènement est fermeture de fenêtre #######
    if window.quit:
        running = False
        pygame.quit()

    # afficher
    window.mainloop()
