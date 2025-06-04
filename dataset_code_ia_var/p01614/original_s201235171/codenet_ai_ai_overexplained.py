def main():
    # Demander à l'utilisateur d'entrer un nombre entier qui sera stocké dans la variable n
    # input() permet de lire l'entrée de l'utilisateur sous forme de chaîne de caractères
    # int() convertit cette chaîne de caractères en un entier
    n = int(input())
    # Créer une liste appelée 'phrase' qui contiendra n éléments
    # Chaque élément est un tuple composé de trois entiers
    # La boucle 'for _ in range(n)' s’exécute n fois, où _ est une variable muette
    # À chaque itération, on lit une ligne d'entrée, on la découpe en mots, on convertit chaque élément en entier (map)
    # Puis on transforme la map en tuple
    phrase = [tuple(map(int, input().split())) for _ in range(n)]
    # Lire un entier m à partir de l'entrée utilisateur
    m = int(input())
    # Initialiser une liste vide appelée 'ans' qui stockera les réponses finales à afficher
    ans = []
    # Initialiser un indicateur/flag à 1 (ceci servira à savoir si on doit afficher le résultat ou non à la fin)
    flag = 1
    # Créer une liste nommée 'dp' de taille 394, initialisée à 0
    # Cette liste servira à mémoriser, pour chaque indice (poids), la valeur maximale pouvant être obtenue
    dp = [0] * 394
    # Parcourir tous les poids possibles de 0 à 392 inclus (car range(393) va jusqu'à 392)
    for w in range(393):
        # Pour chaque poids w, examiner chacune des phrases de la liste 'phrase'
        for i in range(n):
            # Extraire le i-ème tuple de 'phrase'
            t = phrase[i]
            # Décomposer le tuple t en trois variables : s, l et p
            s, l, p = t
            # Si le poids courant w auquel on ajoute s (la première composante du tuple) ne dépasse pas 393,
            # alors on peut mettre à jour la valeur de dp[w + s]
            if w + s <= 393:
                # Mettre à jour dp[w + s] avec la valeur maximale possible entre sa valeur actuelle ou
                # la valeur dp[w] à laquelle on ajoute p (la troisième composante du tuple)
                dp[w + s] = max(dp[w + s], dp[w] + p)
            # Si le poids courant w auquel on ajoute l (la deuxième composante du tuple) est strictement inférieur à 393,
            # alors on met à jour dp[w + l] de la même manière
            if w + l < 393:
                dp[w + l] = max(dp[w + l], dp[w] + p)
            # Sinon, si le poids courant w auquel on ajoute l atteint ou dépasse 393
            # et qu'ajouter s à w donnerait un poids inférieur à 393,
            # alors on met à jour dp[393] (le dernier indice possible de la liste)
            elif w + l >= 393 and w + s < 393:
                dp[393] = max(dp[393], dp[w] + p)
    # Répéter m fois (pour chaque requête utilisateur)
    for _ in range(m):
        # Lire un entier w à partir de l'entrée utilisateur
        w = int(input())
        # Si le flag a été mis à zéro précédemment, on saute cette itération
        if not flag:
            continue
        # Si dp[w] est non nul (autrement dit, une solution existe pour ce poids)
        if dp[w]:
            # Ajouter cette valeur de dp[w] à la liste ans
            ans.append(dp[w])
        else:
            # Sinon, si dp[w] est nul, cela signifie qu'aucune solution n'est possible pour ce poids
            # On passe flag à zéro pour indiquer qu'on ne doit plus rien afficher
            flag = 0
    # Si flag est resté à 1 (aucun poids impossible trouvé)
    if flag:
        # Afficher chaque élément de la liste ans
        for a in ans:
            print(a)
    else:
        # Sinon, afficher simplement -1 puisqu’au moins une requête n’a pas de solution
        print(-1)

# Ce bloc permet de s'assurer que le code contenu dans main() ne s'exécutera
# que si ce fichier est exécuté directement et non importé comme module
if __name__ == "__main__":
    main()