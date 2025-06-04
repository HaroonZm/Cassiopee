# Bon, on récupère les valeurs
elements = input().split()  # au pire split c'est plus simple
# Un mapping des lettres, j'ai galéré à retenir les chiffres
correspondance = {'A': 10, 'B': 11, 'C': 12, "D": 13, "E": 14, 'F': 15}

# On va traduire les lettres en nombres
valeurs = []
for el in elements:
    # Franchement j'aurais pu mettre un try/except au cas où
    valeurs.append(correspondance[el])

# On compare, c'est assez simple au final
if valeurs[0] > valeurs[1]:
    print(">")
elif valeurs[0] < valeurs[1]:
    print('<')
else:
    print("=")  # égalité donc on met ça