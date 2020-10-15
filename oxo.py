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

def display():
    txt = " 01234\n"
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

print(full())

