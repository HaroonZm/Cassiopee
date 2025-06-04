def sort_key(end):
    """
    Génère une clé de tri pour chaque événement de segment.

    Les extrémités de type 'début' sont triées avant les extrémités de type 'fin' au même point,
    en doublant la valeur puis en ajoutant 1 si c'est un début.

    Args:
        end (tuple): Un tuple contenant (valeur, is_start), où
            - valeur (int): la position de l'extrémité
            - is_start (bool): True si c'est un début de segment, False si c'est une fin

    Returns:
        int: La clé de tri numérique
    """
    if end[1]:
        return end[0] * 2 + 1
    return end[0] * 2

# Lecture du nombre d'entiers dans la séquence
n = int(input())
# Lecture de la séquence d'entiers
a = [int(i) for i in input().split()]
# Ajout d'un zéro à la fin pour simplifier le traitement de la séquence
a.append(0)

# Liste pour stocker les extrémités des segments où la séquence décroît
ends = []
# Variable pour mémoriser la valeur maximale lors d'une descente
top = 0
# Flag pour suivre si on est dans une montée (True) ou une descente (False)
up = True

# Parcours de la séquence pour détecter les segments descendants
for i in range(0, n + 1):
    # Si on était en descente et qu'on détecte un changement de tendance ou la fin du tableau
    if not up and (i == n or a[i + 1] > a[i]):
        # On ajoute la fin du segment descendant (avec le vrai a[i]) comme un événement de "début"
        ends.append((a[i], True))
        # On clôture ce segment avec sa valeur de départ top (événement de "fin")
        ends.append((top, False))
        # On repasse en mode montée
        up = True
    # Si on n'est pas à la fin et que la tendance passe de montée à descente
    elif i != n and up and a[i + 1] < a[i]:
        # On mémorise la valeur au sommet qui démarre le segment descendant
        top = a[i]
        # On passe en descente
        up = False

# Trie les extrémités pour que traitement des recouvrements soit correct (ordre des débuts/fin)
ends.sort(key=sort_key)

# Calcul du nombre maximum de segments descendants qui se chevauchent à tout instant
max_overlaps = 0      # Maximum simultané rencontré
overlaps = 0          # Nombre courant de segments ouverts

for end in ends:
    if end[1]:  # Si c'est un début de segment descendant
        overlaps += 1
        if overlaps > max_overlaps:
            max_overlaps = overlaps
    else:       # Si c'est une fin de segment descendant
        overlaps -= 1

# Affichage du nombre maximum de segments descendants qui se recouvrent
print(max_overlaps)