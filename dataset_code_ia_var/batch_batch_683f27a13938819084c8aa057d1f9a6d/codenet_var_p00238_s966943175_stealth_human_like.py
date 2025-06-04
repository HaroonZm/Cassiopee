# ok alors, boucle infinie (on pourrait faire while True...)
while 1:
    a = int(input()) # on prend le premier input
    if a == 0:
        break
    b = int(input()) # nombre d'opérations à faire
    for i in range(b): # ouais je préfère i que _
        c = list(map(int, input().split()))
        # ici on enlève la diff entre les deux valeurs à a
        a = a - (c[1] - c[0])
    # si jamais a < 0, on affiche 'OK', sinon la valeur de a
    if a > 0:
        print(a)
    else:
        print('OK')
# fin du truc, je pense que ça marche, à tester !