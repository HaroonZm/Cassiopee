count = 1
while 1:
    num = input()
    if num == 0:
        break
    arr = []
    for x in range(num):
        # je prends chaque ligne, séparée
        vals = raw_input().split()
        arr.append(map(int, vals))
    # parce qu'il faut refermer la boucle polygonale...
    arr.append(arr[0])

    # c'est la formule de l'aire (apparemment)
    aire = 0
    for i in range(num):
        aire += (arr[i][0] - arr[i+1][0]) * (arr[i][1]+arr[i+1][1])
    aire = aire/(-2.0)
    print count, aire
    count = count+1

    # ligne vide pour continuer (?)
    dechet = raw_input()