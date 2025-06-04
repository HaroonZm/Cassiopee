import sys  # Importe le module 'sys', qui fournit l'accès à certaines variables et fonctions propres à l'interpréteur Python

# Lit une ligne depuis l'entrée standard (au clavier), qui représente le nombre total d'éléments à traiter,
# puis convertit cette chaîne de caractères en entier à l'aide de la fonction int
N = int(input())

# Initialise une liste vide nommée 's' qui servira à stocker les entiers fournis par l'utilisateur
s = list()

# Boucle for qui va de 0 jusqu'à N-1 (donc, pour chaque élément à saisir)
for i in range(N):
    # Lit à chaque itération un entier depuis l'entrée standard et l'ajoute (append) à la liste 's'
    s.append(int(input()))

# Trie la liste 's' par ordre décroissant (du plus grand au plus petit) grâce au paramètre reverse=True du tri
s.sort(reverse=True)

# Calcule la somme totale des éléments de la liste 's' à l'aide de la fonction sum, et stocke le résultat dans la variable 'point'
point = sum(s)

# Calcule la taille de la liste 's' (autrement dit, le nombre total d'éléments dans 's') et la stocke dans la variable 'l'
l = len(s)

# Initialise l'indice de boucle 'i' à 0, qui sera utilisé pour parcourir un certain nombre d'itérations dans la boucle 'while'
i = 0

# Débute une boucle 'while' qui s'exécute tant que 'i' est strictement inférieur à 'l'
while i < l:
    # Vérifie si la somme courante 'point' n'est pas un multiple de 10 (donc son reste modulo 10 est différent de 0)
    if point % 10 != 0:
        # Si c'est le cas, affiche la valeur de 'point' via la fonction print
        print(point)
        # Termine immédiatement l'exécution du programme grâce à sys.exit()
        sys.exit()
    # Vérifie si la liste 's' n'est pas vide
    if not s == []:
        # Parcourt en sens inverse la liste 's' (du dernier au premier élément)
        for x in reversed(list(s)):
            # Pour chaque élément 'x', vérifie si 'x' n'est pas un multiple de 10
            if not x % 10 == 0:
                # Si un tel élément est trouvé, on le retire de la liste 's' à l'aide de pop(),
                # en cherchant son index avec s.index(x), et on le soustrait de 'point'
                point -= s.pop(s.index(x))
                # Importe de sortir immédiatement de la boucle for pour éviter de retirer d'autres éléments pour cette itération
                break
    # Incrémente la valeur de 'i' de 1 pour poursuivre à l'itération suivante de la boucle while
    i += 1

# Si la boucle while se termine sans afficher de somme non multiple de 10, on affiche la chaîne de caractères "0"
print("0")