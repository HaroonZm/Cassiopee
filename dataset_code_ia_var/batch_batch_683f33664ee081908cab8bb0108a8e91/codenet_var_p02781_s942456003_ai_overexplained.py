def run():
    # Lecture de l'entrée utilisateur : 
    # Prend le premier input() comme une chaîne représentant un nombre, 
    # convertit chaque caractère de la chaîne en entier, et stocke la liste d'entiers dans N.
    # Par exemple, si l'utilisateur saisit "123", alors N = [1, 2, 3].
    N = list(map(int, list(input()))
    # Lecture du deuxième input() : attend un entier K saisi par l'utilisateur,
    # qui indique le nombre maximum de chiffres non nuls autorisés.
    K = int(input())
    # Calcul du nombre de chiffres du nombre N (longueur de la liste N)
    Nlen = len(N)
    # Initialisation d'un tableau dynamique dp de 3 dimensions :
    # dp[position][est_plus_petit][compte_chiffres_non_nuls] = nombre de façons
    # position varie de 0 à Nlen inclus, donc il y a (Nlen+1) positions.
    # est_plus_petit est binaire (0 ou 1) et indique si le nombre construit jusqu'à présent
    # est déjà strictement inférieur à N (1) ou toujours égal à sa structure (0).
    # compte_chiffres_non_nuls varie de 0 à K+1 (on utilise K+2 cases pour être sûr de ne jamais dépasser K+1)
    dp = [[[0]*(K+2) for _ in range(2)] for n in range(Nlen+1)]
    # On initialise l'état de départ, où aucun chiffre n'a été choisi, le nombre formé est exactement égal à N, 
    # et on a 0 chiffre non nul utilisé : il n'y a qu'une seule manière de démarrer (penser au nombre vide)
    dp[0][0][0] = 1
    # Boucle sur chaque position du chiffre (pour chaque chiffre de N, de gauche à droite)
    for nlen in range(Nlen):
        # Récupère le chiffre de N à la position courante nlen
        dN = N[nlen]
        # On essaiera toutes les valeurs possibles du chiffre à cette position
        # c'est-à-dire de 0 à 9 inclus
        for d in range(10):
            # On regarde chacun des deux cas possibles pour le drapeau est_plus_petit (j = 0 ou 1)
            for j in range(2):
                # On considère le nombre de chiffres non nuls déjà utilisés k
                for k in range(K+2):
                    # flagj sera le nouveau état "plus petit" après avoir ajouté le chiffre d
                    # Si on était déjà plus petit (j=1), on le reste (donc flagj = 1 peu importe d)
                    # Si on était encore égal (j=0), on devient plus petit si le chiffre choisi d < dN
                    flagj = j or d < dN
                    # S'il n'est *pas* possible de continuer (toujours égal mais on veut mettre un chiffre d > dN),
                    # alors on ne peut pas former un nombre valides dans N - on saute ce cas avec continue
                    if (flagj == 0) and (d > dN):
                        continue
                    # flagk : nouveau nombre de chiffres non nuls après avoir ajouté d :
                    # On ajoute soit 1 si d != 0, soit 0 sinon, mais jamais plus de K+1 (on borne)
                    flagk = min(K+1, k+(d != 0))
                    # On augmente le nombre de façons d'arriver au nouvel état de 1 chiffre plus loin,
                    # en accumulant toutes les transitions possibles depuis l'état précédent
                    dp[nlen+1][flagj][flagk] += dp[nlen][j][k]
    # À la fin, on souhaite le nombre de façons d'obtenir un nombre de K chiffres non nuls
    # qui est au plus N. 
    # Il y a deux cas :
    # - Soit le nombre construit est exactement égal à N (dernier chiffre, flagj=0)
    # - Soit le nombre est strictement inférieur à N (dernier chiffre, flagj=1)
    # On additionne donc ces deux états à la dernière position (dp[-1][0][K] et dp[-1][1][K])
    print(dp[-1][0][K] + dp[-1][1][K])

# Point d'entrée du programme : exécute la fonction run() si ce fichier est le programme principal
if __name__ == '__main__':
    run()