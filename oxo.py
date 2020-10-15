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
    
    ligne = input("ligne(0-4): ")
    ligne = int(ligne)

    while give(colonne, ligne) != ".":
        print(f"la coordonnée {colonne},{ligne} n'est pas dispo !")
        colonne = input("colonne(0-4): ")
        colonne = int(colonne)

        ligne = input("ligne(0-4): ")
        ligne = int(ligne)
    return colonne, ligne
        
def win():
    player = give(x,y)

    if give(x + 1, y) == player:
        if give(x +2, y) == player:
            return True
        if give(x - 1, y) == player:
            return True
    if give(x - 1, y ) == player and give(x - 2, y) == player:
        return True

    if give(x, y + 1) == player:
        if give(x, y + 2) == player:
            return True
        if give(x, y -1) == player:
            return True
    if give(x, y - 1) == player and give(x, y - 2) == player:
        return True

    return False

def display():
    txt = "  01234 \n"
    y = 0
    for ligne in tableau:
        txt += str(y) + " "
        y += 1
        for data in ligne:
            txt += data
        txt += "\n"
    print(txt)

def place(carac, x, y):
    tableau[y][x] = carac
    pass

def give(x,y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return None
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

def load():
    sauve = open("oxo.dat")
    data = sauve.read()
    sauve.close()
    data = data.split("\n")

    for ligne in data:
        del board[0]
        new_ligne = []

        for item in ligne:


def sauvegarde():
    user_sauve = input("Voulez-vous sauvegarder la partie? O/N: ")
    if user_sauve == "O" or user_sauve == "o":
        sauve = open("oxo_sauvegarde.txt", "w")
        lecture = open("oxo.dat")
        data = lecture.read()
        sauvegarde = sauve.write(data)


    


# Le script commence ici

display()

victoire = False

turn = 0
print("-= Init Round =-")
x, y = play()
while True:

    full()
    if full() == True:
        print("Match Nul! :grimacing: ")
        init()
    
    while turn == 0:            
        
        place(PLAYER_1, x, y)
        display()
        turn = 1

    while turn == 1 and win(x, y) == False:
        print("-= Player Two =-")
        player = "Player Two"
        x, y = play()
        place(player1, x, y)
        display()
        win(x, y)
        turn = 2
    while turn == 2 and win(x, y) == False:
        print("-= Player One =- ")
        player = "Player One"
        x, y = play()
        place(player2, x, y)
        display()
        check_victory(x, y)
        turn = 1
    if check_victory(x, y) == True:
        print(f" :star2: {player} Wins  :star2: !")
    
# autre méthode:

victory = False

while not victory:

    print("Player 1:")
    victory = player_plays(player1)

    if victory:
        display()
        print("Player 1 a gagné")
    else:
        print("Player 2:")
        victory = player_plays(player2)

        if victory:
            display()
            print("Player 2 a gagné")

    
        
