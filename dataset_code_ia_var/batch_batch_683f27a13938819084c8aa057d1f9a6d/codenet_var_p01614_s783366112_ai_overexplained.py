def main():
    # Demande à l'utilisateur d'entrer un nombre, puis convertit cette entrée en entier avec int()
    n = int(input())
    # Initialise une liste vidée appelée slp qui contiendra n éléments
    # Chaque élément sera une liste de trois entiers obtenus par input(), split(), map(int, ...) puis convertis en liste
    slp = [list(map(int, input().split())) for _ in [0]*n]
    # Demande un autre entier à l'utilisateur : m
    m = int(input())
    # Crée une liste W de m éléments, chacun étant un entier fourni par l'utilisateur
    W = [int(input()) for _ in [0]*m]
    # Initialise une liste vide ans qui servira à stocker les réponses finales à afficher
    ans = []

    # Initialise une liste point de taille 393 remplie de 0. Cette liste servira à stocker des points maximaux pour des intervalles
    point = [0]*393
    # Parcourt toutes les listes [s, l, p] dans slp
    for s, l, p in slp:
        # Pour chaque i de s à l inclus (donc de s à l, comme la fonction range exclut la borne supérieure, donc l+1)
        for i in range(s, l+1):
            # Met à jour point[i-1] avec la valeur maximale entre sa valeur actuelle et p
            # Cela garantit que pour chaque intervalle, on retient la valeur p la plus élevée applicable à chaque position
            point[i-1] = max(point[i-1], p)
    
    # Initialise une liste memo de taille 394, remplie de 0
    # Cette liste servira à mémoriser les meilleurs scores cumulés pour chaque longueur possible
    memo = [0]*(394)
    # Pour chaque position i de 0 à 392 (393 n'est pas inclus, donc range(393))
    for i in range(393):
        # Pour chaque indice l et valeur p du segment point du début jusqu'à la fin qui permet d'atteindre la fin sans dépasser
        for l, p in enumerate(point[:393-i]):
            # Met à jour memo[i+l+1] : on vérifie si la valeur actuelle (memo[i+l+1]) est inférieure à memo[i] + p (score obtenu en ajoutant ce segment)
            memo[i+l+1] = max(memo[i+l+1], memo[i] + p)
    
    # Pour chaque indice w dans W
    for w in W:
        # Ajoute à ans la valeur de memo[w] (le score maximal obtenu pour la longueur w)
        ans.append(memo[w])
    # Si 0 figure parmi les réponses (cela signifie qu'il n'a pas été possible d'obtenir un score positif pour cette longueur)
    if 0 in ans:
        # Affiche -1 pour indiquer l'impossibilité
        print(-1)
    else:
        # Sinon, pour chaque réponse i dans ans
        for i in ans:
            # Affiche la valeur i (ce qui représente la valeur optimale obtenue pour la longueur demandée)
            print(i)

# Le bloc suivant permet d'exécuter cette fonction main() seulement si le script est exécuté directement,
# c'est-à-dire, pas importé comme un module
if __name__ == '__main__':
    # Appelle la fonction principale du programme
    main()