# Création d'une liste vide nommée 'C' qui servira à stocker les valeurs numériques obtenues après traitement
C = []

# Boucle 'for' qui s'exécute 5 fois, avec la variable 'i' prenant successivement les valeurs 0, 1, 2, 3 et 4
for i in range(5):
    
    # Utilisation de la fonction 'input()' pour demander une entrée utilisateur, 
    # qui est par défaut de type chaîne de caractères (str).
    # La fonction 'int()' convertit cette chaîne en un entier (int).
    X = int(input())
    
    # Condition 'if' qui vérifie si la valeur entière stockée dans 'X' est strictement inférieure à 40
    if X < 40:
        # Si la condition est vraie, l'affectation remplace la valeur de 'X' par 40.
        # Cela permet de garantir que la valeur minimale utilisée sera 40.
        X = 40
    
    # La méthode 'append()' de la liste 'C' ajoute la valeur de 'X' à la fin de cette liste.
    # Ainsi, à chaque itération, on remplit 'C' avec 5 valeurs entières,
    # où chaque valeur est soit celle saisie par l'utilisateur si >= 40, soit 40 sinon.
    C.append(X)
    
# Une fois la boucle terminée et la liste 'C' remplie, on calcule la somme de tous les éléments de 'C' grâce à la fonction 'sum()'.
# Cette somme est ensuite divisée par 5 (nombre total d'éléments) pour obtenir la moyenne.
# L'opérateur '//' est la division entière, qui donne seulement la partie entière du quotient en supprimant toute partie décimale.
print((sum(C)) // 5)