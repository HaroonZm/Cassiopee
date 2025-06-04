# Le point d'entrée principal du programme Python. 
# Cette condition vérifie si ce fichier est exécuté directement (et non importé comme module).
if __name__ == '__main__':
    # Boucle infinie, qui ne sera quittée que si la condition d'arrêt explicite (break) est atteinte plus bas.
    while True:
        # Demande à l'utilisateur une ligne d'entrée, supprime les espaces en début/fin, puis la sépare selon les espaces.
        # map(int, ...) convertit chaque sous-chaîne en entier. list(...) permet d'obtenir une liste d'entiers.
        L, R = list(map(int, input().strip().split()))
        
        # Condition de sortie : Si L et R valent tous les deux 0,
        # cela signifie que nous voulons terminer le programme.
        if L == 0 and R == 0:
            # Sort explicitement de la boucle while.
            break
            
        # Création d'un ensemble (set) contenant la valeur 0. (Un ensemble ne peut contenir de doublons.)
        arr = set([0])
        
        # Si L est strictement supérieur à 0 alors il y a L nombres à lire.
        if L > 0:
            # On demande une nouvelle ligne, qu'on découpe à l'espace, convertit en entiers, et met dans une liste.
            # On ajoute tous les éléments de cette liste à l'ensemble arr (avec .update).
            arr.update(list(map(int, input().strip().split(' '))))
        
        # Même logique que ci-dessus, mais pour R.
        if R > 0:
            arr.update(list(map(int, input().strip().split(' '))))
        
        # On convertit finalement l'ensemble arr en liste puis on trie cette liste dans l'ordre croissant.
        # Cela produira une nouvelle liste ordonnée contenant toutes les valeurs différentes lues précédemment.
        arr = sorted(list(arr))

        # On initialise la variable maxi (qui contiendra le maximum cherché) avec une valeur très petite.
        # Ici : -9999999999 afin que tout écart calculé soit supérieur à cette valeur initiale.
        maxi = -9999999999
        
        # On parcourt tous les indices possibles, sauf le dernier (pas de successeur pour le dernier élément),
        # afin de comparer chaque valeur arr[i] à la suivante arr[i + 1].
        for i in range(len(arr) - 1):
            # On calcule la différence entre deux éléments consécutifs : arr[i+1] - arr[i]
            # On compare cette différence à la valeur courante de maxi 
            # et on garde la plus grande des deux via la fonction max().
            maxi = max(maxi, arr[i + 1] - arr[i])
        
        # Après avoir parcouru tous les couples consécutifs, on imprime (affiche) le maximum trouvé.
        print(maxi)