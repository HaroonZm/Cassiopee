# Demander à l'utilisateur d'entrer un nombre entier, le convertir depuis une chaîne de caractères (input retourne une chaîne) vers un entier
n = int(input())

# Demander à l'utilisateur d'entrer une chaîne de caractères, la stocker dans la variable s
s = input()

# Créer un dictionnaire vide nommé 'hash' qui servira à stocker des couples de chaînes ('red', 'blue') comme clés, et compter leurs occurrences
hash = {}

# La boucle suivante va parcourir tous les entiers possibles de 0 jusqu'à 2^n - 1 en utilisant 'bit' comme variable d'itération
# 1 << n signifie '2 à la puissance n', soit le nombre total de combinaisons binaires sur n bits
for bit in range(1 << n):
    red = ""   # Créer une chaîne vide 'red' qui contiendra certains caractères de 's'
    blue = ""  # Créer une chaîne vide 'blue' qui contiendra d'autres caractères de 's'
    
    # On parcourt chaque position du mot de n caractères, avec la variable 'i' allant de 0 à n - 1
    for i in range(n):
        # Vérifie si le i-ème bit de 'bit' est un (c'est-à-dire égal à 1)
        # (1 << i) crée un nombre qui n'a qu'un seul bit à 1, au rang i (0-based)
        # (bit & (1 << i)) est non-nul si le bit de rang i de 'bit' est à 1
        # > 0 convertit cela en une condition True ou False
        if (bit & (1 << i)) > 0:
            # Le caractère s[i] est ajouté à la chaîne 'red' si le bit est à 1
            red += s[i]
        else:
            # Sinon, le caractère s[i] est ajouté à la chaîne 'blue'
            blue += s[i]
    # On crée un couple (red, blue) et on incrémente de un la valeur associée à cette clé dans le dictionnaire 'hash'
    # hash.get((red, blue), 0) retourne la valeur actuelle, ou 0 si la clé n'existe pas encore
    hash[(red, blue)] = hash.get((red, blue), 0) + 1

# Créer une nouvelle chaîne 't' qui contient la seconde moitié de la chaîne 's' (du n-ième caractère à la fin), inversée
# s[n:] signifie : tous les caractères de s à partir de l'indice n (0-based), jusqu'à la fin
# [::-1] signifie : inverser la chaîne résultante
t = s[n:][::-1]

# Initialiser un compteur 'cnt' à zéro. Il va compter le résultat final.
cnt = 0

# On répète la même méthode d'énumération de toutes les partitions possibles pour la chaîne inversée 't'
for bit in range(1 << n):
    red = ""   # Nouvelle chaîne vide pour 'red'
    blue = ""  # Nouvelle chaîne vide pour 'blue'
    for i in range(n):
        # On utilise le même principe de test de bit pour répartir les caractères de 't' dans 'red' ou 'blue'
        if (bit & (1 << i)) > 0:
            # Ajoute t[i] à 'red' si le i-ème bit de 'bit' est à 1
            red += t[i]
        else:
            # Ajoute t[i] à 'blue' si le bit est à 0
            blue += t[i]
    # Pour chaque partition de la chaîne inversée 't', on cherche dans 'hash' 
    # la clé (blue, red) plutôt que (red, blue), ce qui correspond à échanger les rôles des couleurs
    # La méthode get retourne 0 si la clé n'est pas présente
    cnt += hash.get((blue, red), 0)

# Affiche le résultat final, c'est-à-dire la valeur totale de cnt, dans la sortie standard
print(cnt)