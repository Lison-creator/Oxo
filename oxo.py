player1 = "X"
player2 = "O"

tableau = [
[".", ".", ".",".", "."],
[".", ".", ".",".", "."],
[".", ".", ".",".", "."],
[".", ".", ".",".", "."],
[".", ".", ".",".", "."]
]

# Fonctions

def play():
    #code qui permet à l'utilisateur de choisir une position valide en x et y
    #demander une position en x et en y, vérifier que la position est vide, puis retourner le symb du joueur
    colonne = input("colonne(0-4): " )
    colonne = int(colonne)
    if colonne > 4 and colonne < 0:
        print("Votre placement est hors tableau. La position est comprise entre 0 et 4.")
        colonne = input("colonne(0-4): " )
    
    ligne = input("ligne(0-4): ")
    ligne = int(ligne)
    if ligne > 4 and ligne < 0:
        print("Votre placement est hors tableau. La position est comprise entre 0 et 4.")
        ligne = input("ligne(0-4): " )

    while give(colonne, ligne) != ".":
        print(f"la coordonnée {colonne},{ligne} n'est pas dispo !")
        colonne = input("colonne(0-4): ")
        colonne = int(colonne)

        ligne = input("ligne(0-4): ")
        ligne = int(ligne)
    return colonne, ligne
        
def win():
    win = False
    if play()[0] == tableau[y]

def display():
    txt = " 0 1 2 3 4 \n"
    y = 0
    for ligne in tableau:
        for data in ligne:
            txt += data
        txt += "\n"
    print(txt)

def place(carac, x, y):
    tableau[y][x] = carac
    pass

def give(x,y):
    return tableau[y][x]

def init():
    for n in range(len(tableau)):
        del tableau[0]
        tableau.append([".", ".", ".",".", "."])

def full():
    full = True
    for ligne in tableau:
        for data in ligne:
            if data == ".":
                full = False
    return False
    

# Le script commence ici

place("x", 3, 2)
display()

x, y = play()

place(player1, x, y)
place(player2, x, y)



