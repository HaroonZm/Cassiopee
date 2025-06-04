while True:
    n = int(input())
    if n == 0:
        break
    s = []
    for i in range(n):
        # Pour chaque objet, on lit une ligne de 4 entiers
        ligne = input().split()
        # On convertit chaque string en entier
        obj = []
        for val in ligne:
            obj.append(int(val))
        s.append(obj)

    r_ligne = input().split()
    r = []
    for val in r_ligne:
        r.append(int(val))

    flag = 0
    for i in s:
        if i[1] <= r[0] and i[2] <= r[1] and i[3] <= r[2] and 4 * (i[1] + i[3]) + 9 * i[2] <= r[3]:
            print(i[0])
            flag = 1
    if flag == 0:
        print("NA")