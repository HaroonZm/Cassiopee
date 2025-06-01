import sys

# Définition d'une fonction nommée 'solve' qui prend en entrée deux arguments :
# 'temperatures' : une liste de températures journalières (des entiers)
# 'clothes' : une liste de vêtements, où chaque vêtement est une liste de trois entiers
#             représentant la plage de température acceptable et un point associé.
def solve(temperatures, clothes):
    # Initialisation d'une liste 'points' contenant autant de sous-listes vides
    # que le nombre de températures (un sous-liste par jour)
    # Cette structure permet de stocker les points associés aux vêtements convenant à chaque température.
    points = [[] for _ in range(len(temperatures))]

    # Parcours des températures avec leur indice grâce à enumerate
    # 'i' sera l'indice du jour, 't' la température à ce jour
    for i, t in enumerate(temperatures):
        # Parcours des vêtements dans la liste 'clothes'
        for c in clothes:
            # Vérification si la température 't' est dans la plage acceptable du vêtement 'c'
            # c[0] : température minimale acceptable pour le vêtement
            # c[1] : température maximale acceptable
            if c[0] <= t <= c[1]:
                # Si la température est compatible, on récupère le dernier élément de 'c'
                # qui correspond au nombre de points du vêtement pour ce jour
                # On ajoute ce nombre de points dans la liste 'points[i]' correspondant au jour i
                points[i].append(c[-1])
        # Après avoir examiné tous les vêtements pour ce jour,
        # on trie la liste des points pour ce jour afin d'avoir les points classés par ordre croissant
        points[i].sort()

    # On initialise une liste nommée 'dp' (programmation dynamique) contenant deux sous-listes
    # Chaque sous-liste contient deux éléments : une valeur de points et l'accumulation maximale pour ce point
    # Pour le premier jour, on considère uniquement le minimum et le maximum parmi les points
    # disponibles pour ce jour, avec un score initial de 0 car on débute
    dp = [[min(points[0]), 0], [max(points[0]), 0]]

    # Parcours des jours suivants en passant par chaque sous-liste 'p' de points associés aux vêtements compatibles
    # points[1:] signifie que l'on saute le premier jour qui a déjà été traité
    for p in points[1:]:
        # Mise à jour de la liste 'dp' pour le jour courant
        # Le but est de choisir entre prendre le minimum ou le maximum des points du jour courant
        # pour maximiser la valeur accumulée, en tenant compte de la valeur précédente et des absences de changement de points
        # abs(min(p) - dp[0][0]) correspond à la "distance" entre le nouveau minimum de points et l'ancienne valeur minimale,
        # Soit un "coût" pour passer de l'ancien point à celui-ci.
        # On calcule les scores possibles depuis les deux configurations du jour d'avant (dp[0] et dp[1])
        dp = [
            [min(p), max(dp[0][1] + abs(min(p)-dp[0][0]), dp[1][1] + abs(min(p)-dp[1][0]))],
            [max(p), max(dp[0][1] + abs(max(p)-dp[0][0]), dp[1][1] + abs(max(p)-dp[1][0]))]
        ]

    # Retourne le maximum des valeurs accumulées parmi les deux configurations possibles du dernier jour
    # dp[0][1] : accumulation associée au minimum des points du dernier jour
    # dp[1][1] : accumulation associée au maximum
    # On retourne donc la meilleure accumulation de points possible après avoir parcouru tous les jours.
    return max(dp[0][1], dp[1][1])

# Fonction principale qui sera appelée si le script est exécuté directement
def main(args):
    # Ligne d'entrée : deux entiers, 'd' pour le nombre de jours, 'n' pour le nombre de vêtements
    # On lit une ligne avec input() puis on divise la chaîne obtenue selon les espaces,
    # et on convertit chaque élément en entier grâce à map(int, ...)
    d, n = map(int, input().split())

    # Lecture des températures pour chaque jour, on crée une liste avec une compréhension de liste
    # On lit 'd' lignes, chacune contenant un entier température, que l'on convertit en int et stocke
    temperatures = [int(input()) for _ in range(d)]

    # Lecture des vêtements, chaque vêtement représenté par trois entiers séparés par des espaces
    # On lit 'n' lignes, chaque ligne est divisée en chaînes, converties en int,
    # puis stockées dans une liste représentant un vêtement
    clothes = [[int(x) for x in input().split()] for _ in range(n)]

    # On appelle la fonction 'solve' avec les données récupérées pour obtenir le résultat
    ans = solve(temperatures, clothes)

    # Affichage du résultat final, le score maximum calculé
    print(ans)

# Condition qui vérifie si ce script est exécuté en tant que programme principal
# Cette condition évite d'exécuter le main lors de l'import de ce script comme module
if __name__ == '__main__':
    # Appel de la fonction main, en lui passant les arguments de la ligne de commandes (non utilisés ici néanmoins)
    main(sys.argv[1:])