def solve(string):
    # La fonction 'solve' prend une seule entrée appelée 'string'.
    # 'string' est supposé être une chaîne de caractères contenant deux entiers séparés par un espace.

    # On utilise la méthode 'split()' sur la chaîne 'string'. Cela découpe la chaîne en une liste de sous-chaînes,
    # séparées par des espaces (par défaut, split() sépare selon tout espace blanc).
    # Par exemple, si string = '3 2', alors string.split() retournera ['3', '2'].

    # La fonction 'map' applique la fonction int à chaque élément de la liste résultante.
    # Cela convertit chaque chaîne représentant un entier en véritable entier Python.
    # Exemple: map(int, ['3', '2']) retourne un itérable contenant les entiers 3 et 2.

    # Enfin, l'affectation multiple (n, m) = ... extrait ces deux entiers et les affecte respectivement à n et m.
    n, m = map(int, string.split())

    # Calcul de la réponse selon la formule donnée :
    # (n - m) * 100 + 1900 * m
    # (n-m) calcule la différence entre n et m ; c'est basique, on soustrait deux entiers.
    # On multiplie cette différence par 100, ce qui revient à ajouter 100 fois (n-m).
    # On multiplie ensuite m (le second entier) par 1900.
    # On additionne les deux résultats pour obtenir un total.

    # Ensuite, le tout est multiplié par (2**m).
    # Le symbole ** signifie l'exponentiation en Python. Donc 2**m veut dire 2 à la puissance m.
    # C'est-à-dire, on multiplie le total par deux, m fois. Par exemple, si m=3, 2**3 = 8.

    # Enfin, le résultat de ce long calcul est de type entier (int).
    # On convertit cet entier en chaîne de caractères avec str(), probablement pour faciliter l'affichage.
    return str(((n - m) * 100 + 1900 * m) * (2**m))

# Ceci permet de s'assurer que le code ci-dessous ne s'exécute que si ce fichier est le point d'entrée du programme.
# '__name__' est une variable spéciale dans les modules Python.
# '__main__' est la valeur de '__name__' quand le fichier est exécuté directement, et non importé.
if __name__ == '__main__':
    # La fonction input() lit une ligne de texte entrée par l'utilisateur au clavier (terminée par 'Entrée').
    # La chaîne lue est transmise en tant qu'argument à la fonction 'solve'.
    # La fonction 'solve' calcule le résultat attendu et retourne une chaîne de caractères.

    # La fonction print() affiche ce qui lui est donné en argument à l'écran.
    # Ici, elle affichera le résultat renvoyé par 'solve(input())'.
    print(solve(input()))