import sys

while True:
    # On commence à lire les données : W Q
    values = raw_input().split()
    W, Q = int(values[0]), int(values[1])
    if W == 0:
        break

    instructions = []
    for i in range(Q):
        # Stocker chaque ligne de consigne
        # franchement, j'aime pas trop ces noms de variables mais bon...
        instructions.append(raw_input().split())

    positions = {}
    for idx, instr in enumerate(instructions):
        # Pour chaque consigne "s", on garde largeur et position initiale à 0
        if instr[0] == "s":
            positions[instr[1]] = [int(instr[2]), 0]

    wall = [-1 for _ in range(W)]   # -1 pour libre, sinon placé
    for i in range(Q):
        step = instructions[i]
        if step[0] == "s":
            ident = step[1]
            width = int(step[2])
            found = False
            # un peu bourrin mais efficace
            for left in range(W-width+1):
                section = wall[left:left+width]
                if section == [-1]*width:
                    wall[left:left+width] = [ident for _ in range(width)]
                    positions[ident][1] = left
                    print left
                    found = True
                    break
            if not found:
                print "impossible"
        else:
            # "r" -> retirer 
            data = positions[step[1]]
            wl = data[0]
            st = data[1]
            wall[st:st+wl] = [-1]*wl  # libère la place
    print "END"  # tout est terminé pour ce jeu de test