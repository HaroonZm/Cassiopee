# Demande à l'utilisateur de saisir un entier via l'entrée standard (par défaut, input() retourne toujours une chaîne de caractères)
n = int(input())  # Convertit la chaîne saisie en un entier grâce à la fonction int()

# Demande une deuxième saisie utilisateur sous forme de chaîne de caractères
s = input()  # Cette chaîne correspondra à une séquence de caractères 'o' ou 'x', utilisée dans l'algorithme

# Boucle sur la liste de toutes les combinaisons valides de deux caractères initiaux possibles pour la séquence d'animaux
# Ces combinaisons sont 'SS', 'SW', 'WS' et 'WW' (S pour 'Sheep', W pour 'Wolf' dans la logique du problème)
for c in ['SS', 'SW', 'WS', 'WW']:
    # Pour chaque combinaison initiale possible, on va essayer de déterminer le reste de la séquence
    # La boucle s'exécutera de 1 jusqu'à n-2 (inclus), car les deux premiers animaux sont déjà fixés
    for d in range(1, n - 1):
        # Si à la position d de la séquence c actuelle, on rencontre une "S" (Sheep / Mouton)
        if c[d] == 'S':
            # Si la direction à la position correspondante dans s est 'o' (par exemple, l'animal dit la vérité)
            if s[d] == 'o':
                c += c[d - 1]  # Ajoute à la séquence c le même caractère qui précède (même espèce)
            # Si le caractère précédent est encore un mouton
            elif c[d - 1] == 'S':
                c += 'W'  # Ajoute un loup (Wolf) à la séquence
            else:
                c += 'S'  # Sinon, ajoute un mouton (Sheep) à la séquence
        else:
            # Si à la position 'd' c'est un "W" (Wolf / Loup)
            # Si la direction indiquée par s[d] est 'x' (par exemple, l'animal ment)
            if s[d] == 'x':
                c += c[d - 1]  # Même logique: ajoute à la séquence le caractère précédent
            # Si le caractère précédent est "S" (Sheep)
            elif c[d - 1] == 'S':
                c += 'W'  # Ajoute un loup
            else:
                c += 'S'  # Sinon, ajoute un mouton

    # Après la génération de la séquence c, on va créer une chaîne res qui va reconstituer la chaîne "s" attendue
    res = ''  # Chaîne vide pour stocker la reconstitution
    # Boucle sur chaque index i de la séquence c (qui devrait compter n caractères)
    for i in range(len(c)):
        # On compare l'animal précédent (i-1) et le suivant ((i+1) modulo la longueur, pour gérer le cycle)
        if c[i - 1] == c[(i + 1) - len(c)]:
            # Si ces deux animaux sont identiques
            if c[i] == 'S':
                res += 'o'  # Si l'animal courant est un mouton, il dit la vérité (donc 'o')
            else:
                res += 'x'  # Si c'est un loup, il ment (donc 'x')
        else:
            # Si les deux animaux ne sont pas identiques
            if c[i] == 'S':
                res += 'x'  # Si c'est un mouton, il ment ('x')
            else:
                res += 'o'  # Si c'est un loup, il dit la vérité ('o')
    # A ce stade, res est censé correspondre à la chaîne d'entrée s si la séquence c correspond à la description du problème

    if res == s:
        print(c)  # Si on a reconstruit la chaîne d'origine, on imprime la séquence d'animaux trouvée
        exit()    # Arrête immédiatement le programme (car une solution a été trouvée)

# Si aucune des 4 combinaisons initiales ne donne de résultat, on affiche -1 (pas de solution)
print(-1)