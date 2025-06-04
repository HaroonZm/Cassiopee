# Demande à l'utilisateur de saisir une chaîne de caractères depuis l'entrée standard (clavier)
# La fonction input() lit une ligne de texte. list(input()) transforme cette chaîne en liste de caractères
s = list(input())

# Crée une liste vide qui sera utilisée pour stocker des valeurs intermédiaires
X = []

# Initialise une variable appelée 'hoge' à 0. Cette variable servira à compter le nombre de 'x' consécutifs
hoge = 0

# Commence une boucle for qui itérera sur tous les indices de la liste s (pour chaque caractère de la chaîne saisie)
for i in range(len(s)):
    # Vérifie si le caractère à la position i dans s est égal à 'x'
    if s[i] == 'x':
        # Si c'est un 'x', incrémente (ajoute 1 à) la variable 'hoge'
        hoge += 1
    else:
        # Si ce n'est PAS un 'x' :
        # Ajoute le nombre de 'x' accumulés jusqu'ici (stocké dans 'hoge') à la liste X
        X.append(hoge)
        # Ajoute à la liste X le caractère courant de s (donc un caractère différent de 'x')
        X.append(s[i])
        # Réinitialise le compteur de 'x' à 0 car la séquence de 'x' est terminée
        hoge = 0

# Après avoir parcouru tous les caractères, ajoute à la liste X le dernier nombre de 'x' accumulés
X.append(hoge)

# Crée une variable ans qui servira à stocker la réponse finale (initialisée à 0)
ans = 0

# Lance une seconde boucle for, qui va parcourir la moitié de la liste X (division entière)
# Cela permet de parcourir la liste X du début et de la fin simultanément
for i in range(len(X)//2):
    # Vérifie si l'indice i est pair en utilisant l'opérateur modulo (%)
    if i % 2 == 0:
        # Si i est pair, calcule la différence absolue entre l'élément à la position i
        # et celui à la position symétrique à la fin de la liste (-i-1)
        # Puis ajoute cette valeur à la variable ans
        ans += abs(X[i]-X[-i-1])
    # Si i est impair (i % 2 != 0)
    elif X[i] != X[-i-1]:
        # Compare l'élément à l'indice i et celui à l'indice symétrique (-i-1)
        # Si ces deux valeurs sont différentes, affiche -1
        print(-1)
        # Termine immédiatement le programme avec l'instruction exit()
        exit()

# Affiche la valeur finale de ans (le résultat calculé)
print(ans)