import math  # Importe le module math, qui fournit des fonctions mathématiques standards telles que sqrt.

# Prend un entier en entrée depuis l'utilisateur.
N = int(input())  # Utilise la fonction input() pour lire une chaîne, puis la convertit en entier avec int().

# Définit une fonction pour factoriser un nombre entier et retourner ses facteurs premiers sous forme de dictionnaire.
def ff(x):
    # Calcule la racine carrée entière de x, qui est la plus grande valeur entière qui ne dépasse pas la racine carrée de x.
    L = int(math.sqrt(x))
    
    # Initialise un dictionnaire vide pour stocker les facteurs premiers et leurs puissances.
    FACT = dict()
    
    # Boucle depuis 2 jusqu'à L+1 (inclus), pour vérifier chaque nombre entier comme facteur possible.
    for i in range(2, L + 2):  # L+2 car le range s'arrête avant la borne supérieure.
        # Tant que x est divisible par i (x % i == 0), i est un facteur premier de x.
        while x % i == 0:
            # Incrémente le compteur de la puissance de i dans le dictionnaire FACT.
            FACT[i] = FACT.get(i, 0) + 1  # FACT.get(i, 0) obtient la valeur associée à i, ou 0 si i n'est pas encore présent.
            # Met à jour x en le divisant par i, pour continuer la factorisation.
            x = x // i  # // est la division entière.
    
    # Après la boucle, s'il reste une valeur de x supérieure à 1, c'est un facteur premier également.
    if x != 1:
        FACT[x] = FACT.get(x, 0) + 1
    
    # Retourne le dictionnaire contenant les facteurs premiers et leur exposant.
    return FACT

# Définition de la fonction d'algorithme d'Euclide étendu.
# Cette fonction calcule pour deux entiers a et b, des coefficients x et y
# tels que a*x + b*y = pgcd(a, b), et retourne (x, y) et le pgcd.
def Ext_Euc(a, b, axy=(1, 0), bxy=(0, 1)):
    # Prend deux entiers a et b, et leurs coefficients associés sous forme de tuples
    # Les coefficients initiaux sont (1, 0) pour a, et (0, 1) pour b, représentant la combinaison linéaire des deux entiers.
    
    # Effectue la division euclidienne de a par b pour obtenir le quotient q et le reste r.
    q, r = divmod(a, b)  # divmod(a, b) retourne un tuple (q, r) où q = a // b, r = a % b.
    
    # Si le reste est 0, cela signifie que pgcd(a, b) = b, et bxy contient les bons coefficients pour b.
    if r == 0:
        return bxy, b  # Retourne les coefficients bxy et le pgcd b.
    
    # Sinon, calcule les nouveaux coefficients pour la prochaine itération.
    # rxy sont les coefficients du reste r dans la combinaison linéaire.
    rxy = (axy[0] - bxy[0] * q, axy[1] - bxy[1] * q)
    # Appelle récursivement la fonction avec des paramètres mis à jour pour poursuivre l'algorithme.
    return Ext_Euc(b, r, bxy, rxy)

# Appelle la fonction de factorisation sur 2*N pour obtenir ses facteurs premiers avec leur exposant.
FACT = ff(N * 2)  # FACT est un dictionnaire de la forme {facteur: exposant, ...}

# Initialise une liste vide pour stocker les différentes puissances des facteurs premiers.
LIST = []
# Parcourt les différents facteurs premiers.
for f in FACT:
    # Pour chaque facteur f, ajoute f^exposant (c'est-à-dire f à la puissance FACT[f]) dans la liste.
    LIST.append(f ** FACT[f])

# Stocke le nombre de facteurs premiers distincts (également la taille de LIST).
L = len(LIST)  # Cela servira à parcourir toutes les combinaisons de sous-ensembles de facteurs.

# Initialise la variable qui contiendra la réponse minimale,
# en partant d'une valeur initiale de 2*N - 1, car c'est une borne évidente possible pour la réponse.
LANS = 2 * N - 1

# Parcourt tous les sous-ensembles possibles des facteurs premiers à l'aide de la représentation binaire.
# Il y a 2^L sous-ensembles possibles, donc 1<<L (1 décalé de L bits vers la gauche) donne 2^L.
for i in range(1 << L):  # i parcourt de 0 à 2^L - 1.
    A = 1  # Produit des éléments sélectionnés dans ce sous-ensemble.
    B = 1  # Produit des éléments non sélectionnés dans ce sous-ensemble.

    # Pour chaque bit j, vérifie si ce facteur premier fait partie du sous-ensemble ou non.
    for j in range(L):
        # Si le j-ième bit de i est 1, l'élément est pour A, sinon il est pour B.
        if i & (1 << j) != 0:  # & est le ET binaire. (1 << j) place un 1 à la position j.
            A *= LIST[j]      # Ajoute à A si le bit est à 1.
        else:
            B *= LIST[j]      # Sinon, ajoute à B.
    # Ignore les cas où A ou B égale à 1 (cas dégénérés où tout est dans A ou dans B).
    if A == 1 or B == 1:
        continue  # Passe à l'itération suivante sans exécuter la suite.

    # Applique l'algorithme d'Euclide étendu pour trouver une solution particulière x, y de l'équation : A*x - B*y = 1 (ou similaire).
    # Les coefficients retournés sont pour l'équation A * x + (-B) * y = pgcd(A, -B).
    x, _ = Ext_Euc(A, -B)
    # Récupère x (le coefficient de A) et y (le coefficient de -B, mais y n'est pas utilisé dans la suite).
    x, y = x[0], x[1]  # x[0] est le coefficient de A, x[1] celui de -B.

    # Si x est négatif, on souhaite trouver une valeur positive équivalente modulo B, 
    # c'est-à-dire ajouter suffisamment de fois B pour que x >= 0.
    if x < 0:
        # Calcule le multiple de B nécessaire pour relever x à une valeur positive.
        # abs(x) // B donne combien de fois B tient dans la valeur absolue de x
        # 1 + abs(x)//B garantit qu'on dépasse le seuil
        x += (1 + abs(x) // B) * B

    # Met à jour LANS si x*A (c'est-à-dire la prochaine solution possible pour la propriété cherchée) est plus petite.
    LANS = min(LANS, x * A)

# Affiche la réponse finale minimale trouvée.
print(LANS)  # Affiche le plus petit LANS obtenu selon les critères spécifiés dans la boucle précédente.