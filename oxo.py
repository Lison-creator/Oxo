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

# Le script commence ici

place("x", 3, 2)
display()