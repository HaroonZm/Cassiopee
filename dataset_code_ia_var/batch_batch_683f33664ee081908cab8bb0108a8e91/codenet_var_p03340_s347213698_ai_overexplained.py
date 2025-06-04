# Demande à l'utilisateur d'entrer un entier qui sera stocké dans la variable n.
# Cela représente généralement la taille d'une séquence ou d'un tableau.
n = int(input())

# Demande à l'utilisateur d'entrer une ligne de nombres séparés par des espaces.
# La fonction input() récupère la ligne sous forme de chaîne de caractères.
# split() divise cette chaîne en sous-chaînes pour chaque espace.
# map(int, ...) convertit chaque sous-chaîne en entier.
# Enfin, list(...) convertit l'objet map en une liste de ces entiers et l'assigne à la variable a.
a = list(map(int, input().split()))

# Initialise la variable ans avec la valeur de n.
# ans va probablement servir à compter ou mémoriser un résultat relié à la séquence de nombres.
ans = n

# Initialise s avec la première valeur du tableau a.
# Ici, s va servir à mémoriser une valeur lors des itérations, probablement comme un accumulateur.
s = a[0]

# Initialise r avec 0.
# r est généralement utilisé comme un indice de parcours ou pour représenter un pointeur sur la séquence.
r = 0

# Débute une boucle qui parcourt les indices l de 0 jusqu'à n-2 inclus (car range(n-1) s'arrête à n-2).
# l est l'indice de départ de la sous-séquence étudiée.
for l in range(n - 1):
    # Débute une boucle "while" qui continue tant que deux conditions sont vraies :
    # 1) r est strictement inférieur à n-1, c'est-à-dire qu'on reste dans les bornes du tableau.
    # 2) s & a[r+1] == 0, c'est-à-dire que le "et binaire" entre s et le prochain élément est nul.
    # Le & binaire s'assure qu'aucun bit n'est commun (aucun overlap à 1) entre s et a[r+1].
    while r < n - 1 and not (s & a[r + 1]):
        # Met à jour s en calculant le "ou exclusif" (XOR) binaire entre s et a[r+1], et stocke le résultat dans s.
        # Cela mélange les bits de s et du prochain élément de manière réversible.
        s ^= a[r + 1]
        # Incrémente r de 1. On étend donc notre fenêtre vers la droite.
        r += 1
    # Après la boucle while, ajoute à ans la différence r - l.
    # Cela compte le nombre de sous-tableaux valides qui commencent à l'indice l.
    ans += r - l
    # Met à jour s en retirant l'effet de a[l] avec l'opération XOR (puisque s ^= a[l] défait un XOR précédent).
    # Cela prépare s pour la prochaine itération de la boucle principale.
    s ^= a[l]

# Affiche la valeur finale de ans, le résultat du traitement effectué.
print(ans)