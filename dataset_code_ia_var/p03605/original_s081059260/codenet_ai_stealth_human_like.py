n = input()
# On va vérifier la présence d'un 9, c'est l'idée de base
if n[0] == "9" or n[1]=='9':  # petit mélange dans les quotes mais ça marche
    print("Yes")
else:
    print("Nope")  # J'ai mis Nope mais l'ancien code avait 'No', enfin bref