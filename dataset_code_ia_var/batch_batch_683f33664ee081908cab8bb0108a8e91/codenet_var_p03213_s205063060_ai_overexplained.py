import sys  # Importe le module 'sys' qui fournit un accès à certaines variables utilisées ou maintenues par l’interpréteur Python.
from collections import defaultdict  # Importe 'defaultdict', une sous-classe de dictionnaire qui fournit une valeur par défaut pour les clés non présentes.

# Redéfinit la fonction 'read' pour lire toute l'entrée standard sous forme binaire (bytes).
read = sys.stdin.buffer.read
# Redéfinit la fonction 'readline' pour lire une ligne de l'entrée standard sous forme binaire (bytes).
readline = sys.stdin.buffer.readline

# Définit une fonction lambda 'in_n' qui lit une ligne, la convertit en entier et la retourne.
in_n = lambda: int(readline())
# Définit une fonction lambda 'in_nn' qui lit une ligne, découpe la ligne en éléments séparés par des espaces, convertit chaque élément en entier et les retourne sous forme d'itérable (map).
in_nn = lambda: map(int, readline().split())
# Définit une fonction lambda 'in_nl' identique à 'in_nn' sauf que cette fois, le résultat est stocké dans une liste (list) au lieu d'un objet map.
in_nl = lambda: list(map(int, readline().split()))
# Définit une fonction lambda 'in_na' qui lit toute l'entrée standard, découpe par espaces tous les éléments, les convertit en entiers, et les retourne sous forme d'itérable (map).
in_na = lambda: map(int, read().split())
# Définit une fonction lambda 'in_s' qui lit une ligne, supprime les espaces blancs et les caractères spéciaux de fin de ligne, puis décode les bytes en string UTF-8.
in_s = lambda: readline().rstrip().decode('utf-8')

# Définition d'une fonction pour décomposer un entier en facteurs premiers et renvoyer un dictionnaire contenant ces facteurs et leurs puissances.
def factorize_dict(n):
    b = 2  # Initialisation du plus petit diviseur premier possible, c'est-à-dire 2.
    fct = defaultdict(lambda: 0)  # Création d'un defaultdict avec valeur par défaut 0 pour compter chaque facteur premier.
    # Boucle pour diviser n par tous les entiers possibles b (commençant à 2) tant que b au carré est inférieur ou égal à n.
    while b ** 2 <= n:
        # Boucle interne qui divise n par b tant que n est divisible par b sans reste.
        while n % b == 0:
            n //= b  # Divise n par b et met à jour n avec le quotient.
            fct[b] += 1  # Incrémente le compteur du facteur premier b dans le dictionnaire fct.
        b += 1  # Passe au diviseur suivant.
    # Si après la boucle, il reste un n supérieur à 1, cela signifie que n est un nombre premier lui-même.
    if n > 1:
        fct[n] += 1  # Ajoute ce dernier facteur premier et incrémente son compteur.
    # Retourne le dictionnaire contenant tous les facteurs premiers de départ de n et leurs puissances.
    return fct

# Définition de la fonction principale du programme.
def main():

    N = in_n()  # Lecture de l'entier N à partir de l'entrée standard.

    prime = defaultdict(int)  # Création d'un dictionnaire pour stocker le nombre total d'occurrences de chaque facteur premier dans la décomposition de tous les entiers de 1 à N.

    # Boucle sur tous les entiers de 1 jusqu'à N inclus.
    for i in range(1, N + 1):
        # Pour chaque facteur premier k et son exposant v dans la décomposition de i :
        for k, v in factorize_dict(i).items():
            prime[k] += v  # Incrémente le total d'occurrences pour ce facteur premier k.

    # Définition d'une fonction interne qui compte le nombre de facteurs premiers dans 'prime' ayant un exposant supérieur ou égal à a.
    def num(a):
        # 'prime.values()' récupère tous les exposants, filtre ceux >= a, les convertit en liste, et renvoie la longueur (le nombre d'éléments filtrés).
        return len(list(filter(lambda x: x >= a, prime.values())))

    # Calcul du nombre de façons d'obtenir un diviseur avec au moins 74 facteurs premiers au total.
    ans = num(74)
    # Calcul des combinaisons supplémentaires : au moins un diviseur avec 24 facteurs et au moins un autre avec 2 facteurs (distincts).
    if num(24) >= 1:
        ans += num(24) * (num(2) - 1)
    # Calcul des combinaisons supplémentaires : au moins un diviseur avec 14 facteurs et au moins un autre avec 4 facteurs (distincts).
    if num(14) >= 1:
        ans += num(14) * (num(4) - 1)
    # Calcul des combinaisons : il faut au moins deux diviseurs avec 4 facteurs, et un avec 2 facteurs (tous distincts).
    if num(4) >= 2:
        ans += num(4) * (num(4) - 1) // 2 * (num(2) - 2)
    # Affiche la réponse finale sur la sortie standard.
    print(ans)

# Vérifie si le script est exécuté en tant que programme principal (et non importé comme module).
if __name__ == '__main__':
    main()  # Appelle la fonction principale pour exécuter la logique du programme.