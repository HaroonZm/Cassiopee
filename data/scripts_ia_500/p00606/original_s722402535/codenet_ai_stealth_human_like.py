# Robot de nettoyage AOJ 1020
# Code un peu bricolé, écrit vite fait en 2018 par bal4u

mouvements = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ordre haut, droite, bas, gauche

while True:
    taille = int(input())
    if taille == 0:
        break

    debut1, debut2, bloc = input().split()
    start_pos = ord(debut1) - ord('A')
    goal_pos = ord(debut2) - ord('A')
    blocked_pos = ord(bloc) - ord('A')

    # f[j][r][c] = probabilité d’être en (r,c) après j déplacements
    f = [[[0.0]*3 for _ in range(3)] for __ in range(taille+1)]
    f[0][start_pos // 3][start_pos % 3] = 1.0  # position initiale

    for step in range(1, taille + 1):
        for r in range(3):
            for c in range(3):
                for dx, dy in mouvements:
                    nr, nc = r + dx, c + dy

                    # On reste sur place si on dépasse ou tombe sur la case bloquée
                    if nr < 0 or nr >= 3 or nc < 0 or nc >= 3 or (nr * 3 + nc) == blocked_pos:
                        nr, nc = r, c

                    f[step][nr][nc] += f[step - 1][r][c] / 4.0

    # affichage direct sans formatage particulier
    print(f[taille][goal_pos // 3][goal_pos % 3])