# Définition d'une fonction appelée 'func' qui prend un argument 'n'
def func(n):
    # Vérifie si 'n' est pair (c'est-à-dire, le reste de la division de n par 2 est égal à 0)
    # L'opérateur % est l'opérateur modulo et // est la division entière (renvoie un entier sans décimales)
    # Si n est pair, retourne la moitié de n (n divisé par 2, sans décimales)
    # Sinon (n est impair), retourne trois fois n plus 1 (c'est la règle de Collatz)
    return n // 2 if n % 2 == 0 else 3 * n + 1

# Demande à l'utilisateur de saisir une valeur au clavier avec la fonction input(), qui renvoie une chaîne de caractères
# La fonction int() convertit cette chaîne de caractères en un entier
s = int(input())

# Initialise un compteur 'i' à zéro, qui servira à compter le nombre d'itérations effectuées dans la boucle
i = 0

# Initialise une liste 'sl' qui contient le premier élément 's' (ce sera la liste de tous les termes générés)
sl = [s]

# Démarre une boucle infinie : 'while True' exécute le bloc à l'intérieur indéfiniment, jusqu'à rencontre d'une instruction de sortie comme 'exit()' ou 'break'
while True:
    # Utilise la fonction définie précédemment 'func' avec comme argument le dernier élément de la liste 'sl'
    # sl[-1] désigne le dernier élément de la liste 'sl'
    n = func(sl[-1])
    # Vérifie si la valeur calculée 'n' existe déjà dans la liste 'sl'
    # L'opérateur 'in' vérifie la présence d'un élément dans une séquence (ici, dans la liste)
    if n in sl:
        # Si c'est le cas, affiche i+2 à l'écran avec la fonction print().
        # On ajoute 2 car on commence à compter à partir de 1, et on cherche la première répétition (i commence à 0)
        print(i + 2)
        # Quitte immédiatement le programme avec exit(), ce qui arrête toute exécution ultérieure du script
        exit()
    # Si le nombre 'n' n'est pas encore dans la liste 'sl', l'ajoute à la fin de la liste
    sl.append(n)
    # (Ligne commentée inutile: la ligne suivante retirerait les doublons mais détruirait l'ordre original)
    # sl = list(set(sl))
    # Incrémente le compteur 'i' de 1 à chaque passage dans la boucle (chaque nouveau terme généré)
    i += 1