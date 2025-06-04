import sys  # On importe le module sys, qui permet d'accéder à certaines variables et fonctions propres à l'interpréteur Python
readline = sys.stdin.readline  # On crée une référence à la fonction readline pour lire une ligne de l'entrée standard plus rapidement

# On lit une ligne depuis l'entrée standard et on la convertit en entier, ce sera la valeur de N
N = int(readline())

# On calcule 2^N en utilisant le décalage à gauche (opérateur <<), c'est la même chose que 2**N.
# Par exemple, si N=3 alors 1<<N = 1<<3 = 8.
Ns = 1 << N

# On lit une ligne de chiffre sur l'entrée, on retire les espaces blancs en début/fin avec strip()
# Puis on convertit chaque caractère de la chaîne en entier (map(int, ...))
# Finalement, on crée une liste et on lui ajoute un élément None au début pour que les indices commencent à 1
S = [None] + list(map(int, readline().strip()))

# On lit la ligne suivante, on coupe la chaîne aux espaces, convertit chaque morceau en entier, puis on met le tout dans une liste
P = list(map(int, readline().split()))

# On initialise une liste de taille Ns remplie de None pour stocker diverses permutations de P aux différents états
res = [None] * Ns

# On met P tel quel à l'indice 0 de res, donc res[0] = P
res[0] = P

# Pour res[1], on prend P privé de son premier élément auquel on ajoute ce premier élément à la fin
# Cela correspond à une rotation à gauche de la liste P
res[1] = P[1:] + [P[0]]

# On prépare la liste Ans de taille Ns, remplie de None, qui contiendra les résultats finaux pour chaque état
Ans = [None] * Ns

# On parcourt les indices de 0 à Ns-1 pour traiter toutes les permutations possibles (ou tous les états)
for i in range(Ns):
    ri = res[i]  # On récupère la permutation de P pour l'état i
    leng = len(ri)  # On récupère la longueur de la liste ri (doit rester constante à Ns, puis diminue à chaque niveau)

    # Pour chaque niveau dans le tournoi (on réduit de moitié la longueur à chaque fois)
    # On parcourt 'level' de 0 à nombre de bits nécessaires pour écrire leng, moins 1 (car un tournoi à n éléments à log2(n) niveaux de matches)
    for level in range(leng.bit_length() - 1):
        cnt = []  # On prépare une liste vide pour stocker les gagnants de cette étape

        # On regarde chaque paire consécutive dans la liste ri
        for j in range(len(ri) // 2):
            a = ri[2 * j]      # Premier élément de la paire
            b = ri[2 * j + 1]  # Deuxième élément de la paire

            # On calcule l'indice de la différence absolue entre les deux éléments
            # et on regarde dans la liste S pour savoir quelle est la règle de victoire
            # Si S[abs(a-b)] == 1, alors le plus grand l'emporte, sinon le plus petit
            if S[abs(a - b)] == 1:
                cnt.append(max(a, b))  # On ajoute le plus grand des deux dans cnt si la condition est satisfaite
            else:
                cnt.append(min(a, b))  # Sinon, on ajoute le plus petit des deux

        # On copie la liste cnt pour la prochaine itération (au prochain niveau de tournoi)
        ri = cnt[:]
        lri = len(ri)  # On actualise la longueur de ri (chaque étape réduit de moitié)

        # Ce bloc prépare, selon certaines conditions, les permutations suivantes :
        # Si lri > 1 (donc ce n'est pas la finale), et si Ns // lri (la taille du groupe actuel) dépasse i,
        # alors on crée une nouvelle permutation à l'indice i + Ns//lri avec un décalage circulaire de ri,
        # c'est-à-dire on décale ri d'une place vers la gauche
        if 1 < Ns // lri < Ns - i:
            res[i + Ns // lri] = ri[1:] + [ri[0]]

    # Après toutes les étapes de tournoi pour l'état i, il ne reste qu'un seul gagnant dans ri
    # On place ce gagnant à l'indice i de la liste des réponses
    Ans[i] = ri[0]

# Enfin, on affiche chaque élément de Ans sur une nouvelle ligne, 
# on convertit chaque entier en chaîne de caractères pour pouvoir les joindre avec '\n'
print('\n'.join(map(str, Ans)))