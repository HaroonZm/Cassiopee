# Initialisation d'un compteur à 0
cnt = 0

# La fonction input() lit une entrée utilisateur sous forme de chaîne de caractères.
# int() convertit cette chaîne en entier pour déterminer combien de fois la boucle doit s'exécuter.
# range(n) génère une séquence de n entiers, de 0 à n-1.
# Le "_" est souvent utilisé comme nom de variable quand la valeur n'est pas utilisée.
for _ in range(int(input())):
    # input() lit une nouvelle ligne de l'utilisateur à chaque itération de la boucle.
    # L'expression "input() == 'A'" renvoie True si l'utilisateur a entré "A" et False sinon.
    # En Python, True équivaut à 1 et False à 0 lorsqu'ils sont utilisés comme indices de liste.
    # [-1, 1] est une liste contenant deux éléments : -1 à l'indice 0 et 1 à l'indice 1.
    # Donc, si l'entrée est "A" (True), on utilise l'indice 1 et on ajoute 1 à cnt.
    # Si l'entrée n'est pas "A" (False), on utilise l'indice 0 et on ajoute -1 à cnt.
    cnt += [-1, 1][input() == "A"]
    
    # Vérifie si cnt est devenu négatif après l'ajout précédent.
    if cnt < 0:
        # Si cnt est négatif, cela signifie qu'une condition attendue n'est pas respectée.
        # On affiche "NO" pour indiquer l'échec.
        print("NO")
        # quit() arrête immédiatement l'exécution du programme Python.
        quit()

# Après avoir traité toutes les entrées,
# on utilise l'opérateur ternaire pour déterminer quoi afficher :
# Si cnt est exactement égal à 0, on imprime "YES", sinon "NO".
print("YES" if cnt == 0 else "NO")