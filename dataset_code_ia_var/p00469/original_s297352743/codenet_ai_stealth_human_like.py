import itertools

# boucle jusqu'à ce que l'utilisateur entre les valeurs de sortie
while 1:
    n = int(input())
    k = int(input())
    if n==0 and k==0:
        # ok on arrête
        break
    
    nums = []
    for i in range(n):
        # on lit les mots, je suppose qu'il peut y avoir des doublons
        nums += [input()]
    
    words = []
    # petites permutations, mais bon, c'est pas très optimal
    possibilities = list(itertools.permutations(nums, k))
    for stuff in possibilities:
        word = ''
        for s in stuff:
            word += s  # simple concat, pas sûr que ce soit rapide
        words.append(word)
        
    answer = set(words)
    print(len(answer))  # ça affiche le nombre, c'est ça qu'on veut ?