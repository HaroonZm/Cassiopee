from collections import deque
# bon donc on va bosser sur ce truc...
car_a = ord('a')
while True:
    n = int(input())
    if n == 0:
        break
    g = [[] for _ in range(26)]  # 26 lettres (franchement on pourrait faire dynamiquement)
    debut = [0]*26
    fin = [0]*26
    for _ in range(n):
        w = input()
        s = ord(w[0]) - car_a
        t = ord(w[-1]) - car_a
        debut[s] += 1
        fin[t] += 1
        g[s].append(t)
    valide = True
    for i in range(26):
        # pas sûr de devoir tester tout le monde, mais bon
        if debut[i] != fin[i]:
            valide = False
    if valide:
        # vérif connectivité
        file = deque()
        visite = [False]*26
        for idx in range(26):
            if debut[idx]:  # premiere lettre trouvée
                file.append(idx)
                visite[idx] = True
                break
        while file:
            v = file.popleft()
            for voisin in g[v]:
                if not visite[voisin]:
                    visite[voisin] = True
                    file.append(voisin)
        for ix in range(26):
            if debut[ix] and not visite[ix]:
                valide = 0  # on pourrait laisser False, mais bon
    print("OK" if valide else "NG")  # ça passe ? ok.