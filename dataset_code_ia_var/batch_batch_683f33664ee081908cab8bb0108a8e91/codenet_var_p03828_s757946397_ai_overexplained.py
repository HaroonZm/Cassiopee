# Demande à l'utilisateur de saisir une valeur, puis convertit cette entrée en un entier
n = int(input())

# Vérifie si le nombre saisi est égal à 1
# Si c'est le cas, affiche 1 et termine immédiatement l'exécution du programme
if n == 1:
    print(1)
    exit()  # Arrête le script

# Définit une fonction pour effectuer la factorisation première d'un entier n
def factorization(n):
    # Initialise une liste vide pour stocker les facteurs premiers et leurs puissances correspondantes
    arr = []
    # Crée une copie temporaire de n pour être modifiée sans altérer la variable originale
    temp = n
    # Parcourt tous les entiers i allant de 2 à la racine carrée de n, arrondie à l'entier supérieur, inclus
    # La racine carrée de n est calculée comme n**0.5 ; pour être sûr de ne rien oublier, on utilise la formule de plafond avec des divisions flottantes
    for i in range(2, int(-(-n**0.5 // 1)) + 1):  # -(-x//1) équivaut à math.ceil(x) mais sans importer math
        # Si temp est divisible par i sans reste
        if temp % i == 0:
            # Initialise un compteur à zéro pour compter la multiplicité de ce facteur
            cnt = 0
            # Tant que temp est encore divisible par i
            while temp % i == 0:
                # Incrémente le compteur pour chaque division entière
                cnt += 1
                # Divise temp par i en utilisant la division entière (//) pour éliminer le facteur i à chaque fois
                temp //= i
            # Ajoute le facteur premier i ainsi que la puissance cnt à la liste arr sous forme de sous-liste [facteur, puissance]
            arr.append([i, cnt])
    # Après la boucle, si temp n'est pas redevenu 1, cela signifie qu'il reste un facteur premier > sqrt(n)
    if temp != 1:
        # Ajoute ce facteur restant avec une puissance de 1
        arr.append([temp, 1])
    # Si la liste arr est vide, cela signifie que n était probablement premier
    if arr == []:
        # Ajoute [n, 1] comme unique facteur
        arr.append([n, 1])
    # Retourne la liste des facteurs et puissances
    return arr

# Initialise deux listes vides, destinées à stocker séparément :
# - 'so' : les facteurs premiers uniques rencontrés jusqu'à présent
# - 'ka' : la puissance totale accumulée de chaque facteur premier (indexé en parallèle à 'so')
so = []
ka = []

# Boucle sur tous les entiers de 2 à n inclus (soit n-1 itérations si n>=2)
for i in range(2, n + 1):
    # Effectue la factorisation premier du nombre courant i
    a = factorization(i)
    # Parcourt chaque facteur premier j retourné sous forme de [facteur, puissance]
    for j in a:
        # Si ce facteur premier n'a jamais été vu (pas dans la liste so)
        if not j[0] in so:
            # Ajoute ce facteur premier à la liste so
            so.append(j[0])
            # Ajoute la puissance correspondante à la liste ka (même index que so)
            ka.append(j[1])
        else:
            # Sinon (ce facteur a déjà été vu), augmente la puissance totale de ce facteur à l'index correspondant
            ka[so.index(j[0])] += j[1]

# Initialise une variable pour enregistrer le résultat final (il s'agit du produit des (puissance+1) pour chaque facteur premier)
ans = 1

# Boucle sur chaque puissance accumulée de chaque facteur premier dans la liste ka
for i in ka:
    # Multiplie ans par (puissance + 1), puis applique le modulo 1000000007 (pour éviter les nombres trop grands)
    ans *= (i + 1) % 1000000007

# Affiche le résultat, avec un dernier modulo 1000000007 comme sécurité supplémentaire
print(ans % 1000000007)