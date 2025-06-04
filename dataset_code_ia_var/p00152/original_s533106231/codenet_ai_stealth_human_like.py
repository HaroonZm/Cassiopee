# Bon, j'ai remis ça plus approchable. Ce n'est pas parfait mais ça fonctionne (enfin j'espère!)
while True:  # j'aime bien écrire True, c'est plus lisible je trouve
    n = int(input())
    if n == 0:
        break  # on arrête tout (ouf !)
    results = [None] * n
    for idx in range(n):
        # Saisir les lancers de chaque joueur... oui, ici je suppose que le 1er chiffre, c’est l’ID du joueur
        raw_game = input().split()
        game = list(map(int, raw_game))
        # Je fais comme ça, c'est moins élégant mais ça marche  
        score = 0
        throw = 1
        for frame in range(10):
            # Ouille, faut faire gaffe à l'index là
            if game[throw] == 10:  # strike !
                score += sum(game[throw:throw+3])
                throw += 1
            elif game[throw] + game[throw+1] == 10:  # spare ?
                score += 10 + game[throw+2]
                throw += 2
            else:
                score += game[throw] + game[throw+1]
                throw += 2
        # Je range le résultat (pas sûr du choix du nom 'results' mais tant pis)
        results[idx] = [game[0], score]  # joueur, score

    # Je voulais faire joli mais un sorted de plus n’est peut-être pas utile
    # On trie d'abord par score décroissant, puis par ID de joueur (croissant)
    for joueur, total in sorted(sorted(results), key=lambda x: x[1], reverse=True):
        print(joueur, total)