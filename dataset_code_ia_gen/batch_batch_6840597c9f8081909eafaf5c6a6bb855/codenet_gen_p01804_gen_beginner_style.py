def read_block():
    block = []
    for _ in range(2):
        row1 = input()
        row2 = input()
        block.append(list(row1))
        block.append(list(row2))
    return block

def rotate(block):
    # inutile pour ce problème, pas demandé
    return block

def can_place(field, block, h, x, y):
    # vérifier que le bloc à la hauteur h, position x,y ne dépasse pas du champ horizontal (2x2 cases)
    # et ne rentre pas en collision avec des blocs existants
    for dz in range(2):
        for dx in range(2):
            for dy in range(2):
                if block[dz*2+dx][dy] == '#':
                    fh = h + dz
                    fx = x + dx
                    fy = y + dy
                    # champ: hauteur >=0, horizontale 2x2 (x in 0..0, y in 0..1 ?)
                    # Le champ horizontal est 2x2, donc x,y doivent être 0 ou 0 (?), mais on peut seulement déplacer horizontalement
                    # En fait, la position ne peut dépasser le champ 2x2 en horizontal, donc x,y=0 car champ 2x2
                    if fx < 0 or fx > 1 or fy < 0 or fy > 1:
                        return False
                    if fh < len(field):
                        if field[fh][fx][fy] == '#':
                            return False
    return True

def add_block(field, block, h, x, y):
    for dz in range(2):
        for dx in range(2):
            for dy in range(2):
                if block[dz*2+dx][dy] == '#':
                    fh = h + dz
                    fx = x + dx
                    fy = y + dy
                    while fh >= len(field):
                        # étendre le champ si besoin (zones vides)
                        field.append([['.' for _ in range(2)] for _ in range(2)])
                    field[fh][fx][fy] = '#'

def check_and_delete_line(field):
    deleted = 0
    new_field = []
    for layer in field:
        full = True
        for x in range(2):
            for y in range(2):
                if layer[x][y] != '#':
                    full = False
                    break
            if not full:
                break
        if not full:
            new_field.append(layer)
        else:
            deleted += 1
    # Ajouter des couches vides en haut pour garder la même hauteur
    for _ in range(deleted):
        new_field.append([['.' for _ in range(2)] for _ in range(2)])
    return new_field, deleted

def drop_block(field, block):
    # essayer les positions horizontales: (x,y) = (0,0) seulement possible, mais selon problème on peut faire plusieurs positions pour déplacer horizontalement
    # Le champ horizontal est 2x2, donc la position doit contenir le bloc 2x2 à l'intérieur. Donc x,y=0,0
    # Cependant, on peut déplacer le bloc horizontalement, or le champ horizontal est 2x2, donc il n'y a qu'une seule position (0,0)
    # Mais la description semble dire on peut le déplacer horizontalement pour éviter qu'il sorte du champ
    # Donc, seulement (0,0) possible.

    # Pour être sûr, on va essayer de déplacer horizontalement sur 0 ou 1 (par exemple)
    positions = []
    # Le bloc 2x2x2 doit entrer dans champ 2x2 horizontalement (x,y), donc x,y=0 seulement
    # Donc une seule position possible (0,0)
    positions = [(0,0)]

    max_cleared = 0
    res_field = None

    for pos in positions:
        x, y = pos
        # faire tomber le bloc
        h = len(field)
        while True:
            if not can_place(field, block, h-1, x, y):
                break
            h -=1
        h +=1 # on revient à la dernière bonne position
        if h <0:
            h = 0
        new_field = [ [line[:] for line in layer] for layer in field]
        add_block(new_field, block, h, x, y)

        cleared_lines = 0
        while True:
            new_field, d = check_and_delete_line(new_field)
            if d == 0:
                break
            cleared_lines += d
        if cleared_lines > max_cleared:
            max_cleared = cleared_lines
            res_field = new_field
    return max_cleared, res_field

def main():
    while True:
        line = input()
        if line == '':
            continue
        H, N = map(int, line.split())
        if H == 0 and N == 0:
            break
        field = []
        for _ in range(H):
            c11 = input()
            c12 = input()
            c21 = input()
            c22 = input()
            layer = [[c11[0], c12[0]], [c21[0], c22[0]]]
            # En fait, la lecture c11, c12, c21, c22 correspond chacun à une ligne 2 chars
            # Bug ici: il faudrait les lire correctement: chaque ligne 2 chars
            # On va relire comme ci-dessous:
        field = []
        for _ in range(H):
            rows = []
            for __ in range(2):
                rows.append(input())
            layer = []
            for r in rows:
                layer.append(list(r))
            field.append(layer)
        blocks = []
        for _ in range(N):
            block_layer = []
            for __ in range(4):
                row = input()
                block_layer.append(row)
            block = []
            for i in range(2):
                block.append(list(block_layer[i]))
                block.append(list(block_layer[i+2]))
            blocks.append(block)
        total_cleared = 0
        for block in blocks:
            cleared, field = drop_block(field, block)
            total_cleared += cleared
        print(total_cleared)

if __name__ == "__main__":
    main()