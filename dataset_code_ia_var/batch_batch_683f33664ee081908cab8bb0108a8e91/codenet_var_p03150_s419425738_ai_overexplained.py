# Demander à l'utilisateur d'entrer une chaîne de caractères et stocker cette chaîne dans la variable 's'.
s = input()

# Calculer la longueur de la chaîne de caractères 's' en utilisant la fonction len().
# Cette longueur est stockée dans la variable 'n'. Cela permet de savoir combien de caractères il y a dans la chaîne.
n = len(s)

# Démarrer une boucle externe utilisant la variable 'i' comme index de départ.
# La fonction range(n) génère des entiers de 0 jusqu'à n-1.
# Cela veut dire que 'i' prendra successivement toutes les valeurs possibles d'indices de la chaîne 's'.
for i in range(n):
    # Pour chaque valeur de 'i', démarrer une boucle interne utilisant la variable 'j' comme index de fin.
    # On utilise range(i, n) pour que 'j' commence à la même valeur que 'i' puis aille jusqu'à n-1.
    # Cela permet d'envisager tous les couples (i, j) tels que 0 <= i <= j < n.
    for j in range(i, n):
        # Créer une nouvelle chaîne temporaire 'tmp' en retirant de 's' tous les caractères entre les indices i (inclus) et j (exclus).
        # s[:i] donne la sous-chaîne qui commence au début de 's' et se termine juste avant l'indice 'i'.
        # s[j:] donne la sous-chaîne qui commence à l'indice 'j' et va jusqu'à la fin de 's'.
        # En concaténant ces deux sous-chaînes, on "supprime" les caractères de 's' allant de l'indice 'i' à l'indice 'j-1' inclus.
        tmp = s[:i] + s[j:]

        # Vérifier si la chaîne temporaire 'tmp' est exactement égale à la chaîne de caractères "keyence".
        # Cela signifie que, si l'on retire exactement les lettres entre les indices i et j-1 de 's', on obtient "keyence".
        if tmp == "keyence":
            # Si la condition est vraie (c'est-à-dire si tmp est égal à "keyence") :
            # Afficher "YES" à l'écran pour indiquer qu'il est possible d'obtenir "keyence" en supprimant une sous-chaîne de 's'.
            print("YES")
            # Arrêter immédiatement l'exécution du programme grâce à la fonction quit().
            quit()

# Si aucune des suppressions de sous-chaîne n'a permis d'obtenir "keyence", alors la boucle se termine sans avoir trouvé de solution.
# Dans ce cas, afficher "NO" pour signaler qu'il est impossible d'obtenir "keyence" en supprimant une sous-chaîne de 's'.
print("NO")