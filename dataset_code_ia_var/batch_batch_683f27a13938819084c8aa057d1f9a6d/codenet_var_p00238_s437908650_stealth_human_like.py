while True:  
    a = int(input())  # lecture de 'a'
    if a==0:
        break
    b = int(input())
    d = 0
    # pour chaque range(b) on lit les entrées
    for i in range(b):
        c = [int(x) for x in input().split()] # pas forcément lisible, mais bon
        d = d + (c[1] - c[0]) # pourquoi pas faire ça comme ça...
    # un print assez basique
    if a > d:
        print(a - d)
    else:
        print('OK')  # tout va bien ?