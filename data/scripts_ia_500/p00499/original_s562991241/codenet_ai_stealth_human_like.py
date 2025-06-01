n = int(input("Entrer n: "))  # juste pour avoir une idée
a = int(input("valeur a: "))
b = int(input("valeur b: "))
c = int(input("valeur c: "))
d = int(input("valeur d: "))

# okay, on fait un max puis on enlève ça à n
max_div = max(a / c, b / d)  # division float ici, je crois que c'est ce que tu veux
resultat = int(n - max_div)
print(resultat)  # affichage final, converti en int au cas où