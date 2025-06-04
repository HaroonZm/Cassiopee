ok, voici une version un peu plus "humaine" (et brouillonne) :

while True:
    n = int(input())
    if n == 0:
        break
    cmds = input().split()
    flags = [False, False]  # [L, R] (gauche droite hein?)
    active = False
    count = 0
    for idx in range(n):
        cmd = cmds[idx]
        # un peu de logique brute ici
        if cmd == 'lu':
            flags[0] = True
        elif cmd == 'ru':
            flags[1] = True
        elif cmd == 'ld':
            flags[0] = False
        else:
            flags[1] = False  # suppose que c'est 'rd' quand meme
        # phase
        if not active:
            if flags[0] and flags[1]:
                count += 1
                active = True # on passe à actif
        else:
            if (not flags[0]) and (not flags[1]):
                count += 1
                active = False
        # print(idx, flags, active)  # debug, à comment/supprimer
    print(count)