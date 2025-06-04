# Demander à l'utilisateur de saisir trois entiers séparés par des espaces.
# La fonction input() lit une ligne de texte de l'utilisateur.
# La méthode split() divise cette ligne en une liste de sous-chaînes (ici, sous forme de chaînes de caractères) en utilisant l'espace comme séparateur.
# La fonction map(int, ...) applique la conversion en entier à chaque sous-chaîne pour obtenir des entiers.
# La fonction list(...) convertit le résultat en une liste réelle contenant trois éléments.
# L'affectation multiple permet de décomposer la liste en trois variables distinctes : a, b et n.
a, b, n = list(map(int, input().split()))

# Vérifier si le reste de la division entière de n par 500 n'est pas égal à zéro.
# Cela signifie que n n'est pas un multiple exact de 500.
if n % 500 != 0:
    # Si c'est le cas, ajuster n en l'arrondissant au multiple de 500 immédiatement supérieur.
    # n % 500 donne le reste de la division de n par 500.
    # 500 - n % 500 calcule combien il manque pour arriver au prochain multiple de 500.
    # On ajoute ce montant à n pour obtenir ce multiple.
    n = n + 500 - n % 500

# Vérifier si a est supérieur ou égal à deux fois b.
# Cela compare le coût de a avec le double de b.
if a >= b * 2:
    # Si c'est vrai, il est plus rentable (ou égal) d'utiliser des paquets de 500 à chaque fois.
    # n // 500 calcule combien de fois 500 rentre dans n (division entière).
    # Multiplier ce nombre par b donne le nombre total à payer avec des paquets de 500.
    print((n // 500) * b)
# Si la première condition n'est pas vérifiée, vérifier si a est inférieur à b.
elif a < b:
    # Si coûte moins cher de prendre a (paquet de 1000) que b (paquet de 500).
    # Vérifier si n n'est pas déjà un multiple de 1000.
    if n % 1000 != 0:
        # Arrondir n au multiple de 1000 supérieur pour prévoir assez de paquets.
        n = n + 1000 - n % 1000
    # n // 1000 donne le nombre de paquets de 1000 nécessaires.
    # Multiplier ce nombre par a pour connaître le coût total.
    print((n // 1000) * a)
# Dernier cas: ni a >= 2*b ni a < b ⇒ b <= a < 2b
else:
    # Calculer combien de paquets de 1000 sont nécessaires.
    packages_1000 = n // 1000  # n divisé par 1000 donne le nombre de paquets de 1000 complètement remplis.
    # Calculer combien de paquets de 500 sont nécessaires pour le reste après avoir utilisé des paquets de 1000.
    packages_500 = (n % 1000) // 500  # Le reste n % 1000 est la portion restante. Division entière par 500 donne les paquets de 500 nécessaires.
    # Le coût total est les paquets de 1000 à a (1000-unité) plus les paquets de 500 à b (500-unité).
    print((packages_1000 * a) + (packages_500 * b))