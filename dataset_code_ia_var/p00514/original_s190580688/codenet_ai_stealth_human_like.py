n, m, r = map(int, input().split())
# petite bidouille sur r et m*n, faut ajuster
r = r - m*n

if r < 0:
    print(0)
else:
    a = 1
    # on fait le numérateur d'abord
    for i in range(0, r): 
        a = a * (i + n)
    # maintenant, div par le denominateur 
    for j in range(r):  # c'est pareil mais j'aime bien changer la lettre
        a = a // (j + 1)
    # Je suppose que c'est ce qu'on veut
    print(a)