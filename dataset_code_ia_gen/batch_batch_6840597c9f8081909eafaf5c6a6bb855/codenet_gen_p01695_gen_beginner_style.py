while True:
    n = int(input())
    if n == 0:
        break
    lines = [input() for _ in range(n)]
    depth_list = []
    names = []
    for line in lines:
        d = 0
        while d < len(line) and line[d] == '.':
            d += 1
        depth_list.append(d)
        names.append(line[d:])
    # On traite la première ligne directement
    print(names[0])
    for i in range(1, n):
        d = depth_list[i]
        # on remplace tous les '.' par ' ' sauf le dernier '.' qui devient '+'
        # puis on remplace entre les '+' verticaux par '|'
        arr = []
        for _ in range(d - 1):
            arr.append(' ')
        arr.append('+')
        # Maintenant gérer les '|' selon les règles
        # On regarde les ancêtres directs : entre parent et current, à chaque niveau on regarde si on est dernier enfant
        # Ici, une manière simple:
        # pour les positions de 0 à d-2, on remplace ' ' par '|' si un frère suit au même niveau
        for j in range(d - 1):
            # vérifier si un autre frère existe au niveau j, entre current et parent
            # La règle du problème: entre les '+' --> '|' s'il y a d'autres branches au même niveau
            # En fait on doit regarder s'il y a un frère à ce niveau plus bas à droite
            # Implémentation simple : si un frère existe à même profondeur j+1 sur les lignes suivantes
            # ça indique qu'il faut un '|'
            depth_check = j + 1
            found = False
            for k in range(i + 1, n):
                if depth_list[k] == depth_check:
                    found = True
                    break
                elif depth_list[k] < depth_check:
                    break
            if found:
                arr[j] = '|'
        print(''.join(arr) + names[i])