# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier
# La fonction input() attend que l'utilisateur entre quelque chose et appuie sur Entrée
# La chaîne saisie est stockée dans la variable 's'
s = input()

# On va maintenant vérifier si le premier, le deuxième et le troisième caractère de la chaîne sont identiques
# s[0] correspond au premier caractère de la chaîne (l'indice commence à 0 en Python)
# s[1] correspond au deuxième caractère
# s[2] correspond au troisième caractère
# L'expression s[0] == s[1] == s[2] vérifie deux choses :
# D'abord, elle vérifie si s[0] est égal à s[1], puis, si ce résultat est vrai, elle vérifie si s[1] est aussi égal à s[2]
if s[0] == s[1] == s[2]:
    # Si la condition est vraie, cela signifie que les 3 premiers caractères de la chaîne sont identiques
    # Dans ce cas, on affiche "No" à l'écran avec la fonction print()
    print("No")
else:
    # Si la condition n'est pas remplie (au moins un caractère parmi les trois est différent),
    # on entre dans la section else
    # La fonction print() affiche alors "Yes" à l'écran
    print("Yes")