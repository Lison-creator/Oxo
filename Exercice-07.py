#récupérer des données dans le fichier File_5.txt
#demander à l'utilisateur des données
#
save = open("file_5.txt")
data = save.read()
save.close()

data = data.split(" ")

print(data)

index = input("Où veux-tu insérer ta donnée: ")
index = int(index)

new = input("Quel est la donnée que tu veux insérer: ")

data.insert(index, new)

data_txt = ""

for item in data:
    data_txt += str(item) + " "

data_txt =  data_txt[:-1]

save = open("file_5.txt", "w")
save.write(data_txt)
save.close()
