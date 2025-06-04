while True:
    HP_init, HP_max = map(int, input().split())
    if HP_init == 0 and HP_max == 0:
        break
    R, C = map(int, input().split())
    cave = [list(input()) for _ in range(R)]

    T = int(input())
    trap_damage = {}
    for _ in range(T):
        line = input().split()
        trap_damage[line[0]] = int(line[1])

    S = int(input())
    moves = []
    for _ in range(S):
        d, n = input().split()
        moves.append((d, int(n)))

    P = int(input())
    potions = [int(input()) for _ in range(P)]

    # Starting position and HP
    x, y = 0, 0
    HP = HP_init

    # For movement directions
    dx = {'U':-1, 'D':1, 'L':0, 'R':0}
    dy = {'U':0, 'D':0, 'L':-1, 'R':1}

    # Function to use potions to maximize HP before entering a cell
    def use_potions(hp):
        hp_possible = set([hp])
        for p in potions:
            new_hp_possible = set()
            for val in hp_possible:
                # use potion or not
                new_val = val + p
                if new_val > HP_max:
                    new_val = HP_max
                new_hp_possible.add(val)
                new_hp_possible.add(new_val)
            hp_possible = new_hp_possible
        return max(hp_possible)

    alive = True
    for d, n in moves:
        for _ in range(n):
            nx = x + dx[d]
            ny = y + dy[d]
            # use potions before entering
            HP = use_potions(HP)
            # enter cell
            trap = cave[nx][ny]
            damage = trap_damage.get(trap, 0)
            HP -= damage
            if HP <= 0:
                alive = False
                break
            x, y = nx, ny
        if not alive:
            break

    if alive and HP > 0:
        print("YES")
    else:
        print("NO")