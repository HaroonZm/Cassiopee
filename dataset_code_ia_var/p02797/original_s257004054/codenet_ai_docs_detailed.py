def generate_sequence(n, k, s):
    """
    Génère une séquence de n entiers où :
    - exactement k éléments sont égaux à s,
    - les (n - k) autres éléments sont fixés à une valeur évitant la duplication inutile de s,
    conformément aux contraintes du problème (ex : pour certains problèmes de codeforces, éviter d'avoir tous les éléments identiques).

    Si s n'est pas égal à 10**9, les éléments restants valent 10**9.
    Si s vaut 10**9, les éléments restants valent 1, pour rester dans la plage [1, 10**9].

    Args:
        n (int): Taille totale de la séquence.
        k (int): Nombre d'éléments devant valoir s.
        s (int): Valeur fixée pour k éléments.

    Returns:
        list : Une liste de n entiers contenant exactement k fois s, et (n-k) valeurs convenablement choisies.
    """
    if s != 10 ** 9:
        # Si s est différent de 10**9, on utilise 10**9 pour remplir le reste afin d'éviter des valeurs égales à s.
        ans = [s] * k + [10 ** 9] * (n - k)
    else:
        # Si s vaut 10**9, pour éviter tout débordement on utilise 1 comme valeur de remplissage.
        ans = [s] * k + [1] * (n - k)
    return ans

# Lecture des données d'entrée sous la forme de trois entiers séparés par des espaces.
n, k, s = map(int, input().split())

# Génération de la séquence selon les contraintes.
result_sequence = generate_sequence(n, k, s)

# Affichage du résultat sous forme d'espace entre les éléments.
print(*result_sequence)