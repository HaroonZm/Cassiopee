def get_num(top):
    table = {
        1: lambda: [5, 4],
        2: lambda: [6, 4],
        3: lambda: [6, 5],
        4: lambda: [6, 5],
        5: lambda: [6, 4],
        6: lambda: [5, 4]
    }
    if top in table:
        return table[top]()
    else:
        return []

def get_dir(num, front, top):
    # Impératif et fonctionnel mêlés façon mélange
    if num == front:
        return ["F", num]
    if num == 7 - front:
        return ["B", num]
    stay = lambda conds: any(cond for cond in conds)
    # Mix avec old style
    if num == 4:
        if stay([(front, top) in [(1,5), (5,6), (6,2), (2,1)]]):
            return ["L", num]
        elif stay([(front, top) in [(5,1), (6,5), (2,6), (1,2)]]):
            return ["R", num]
    if num == 5:
        if (front, top) in [(1,3), (3,6), (6,4), (4,1)]:
            return ["L", num]
        elif (front, top) in [(3,1), (6,3), (4,6), (1,4)]:
            return ["R", num]
    if num == 6:
        arr_left = [(2,4), (4,5), (5,3), (3,2)]
        arr_right = [(4,2), (5,4), (3,5), (2,3)]
        if (front, top) in arr_left:
            return ['L', num]
        if (front, top) in arr_right:
            return ['R', num]
    return None

def can_roll(direction, nowi, nowj, maps):
    vect = {'F':(1,0), 'B':(-1,0), 'R':(0,1), 'L':(0,-1)}
    i_shift, j_shift = vect.get(direction, (0,0))
    try:
        if maps[nowi][nowj][0] >= maps[nowi + i_shift][nowj + j_shift][0] + 1:
            return True
    except: # mauvais indices: mur implicite
        pass
    return False

def roll(maps, nowi, nowj, top, front):
    roll_num = get_num(top)
    dirs = [get_dir(roll_num[0], front, top), get_dir(roll_num[1], front, top)]
    for dirinfo in dirs:
        if dirinfo:
            direction, newtop = dirinfo
            vect = {'F':(1,0), 'B':(-1,0), 'R':(0,1), 'L':(0,-1)}
            i_shift, j_shift = vect[direction]
            nfront = front
            if direction == 'F': nfront = top
            elif direction == 'B': nfront = 7 - top
            # on s'arrête au premier possible
            if can_roll(direction, nowi, nowj, maps):
                return roll(maps, nowi + i_shift, nowj + j_shift, 7 - newtop, nfront)
    maps[nowi][nowj][0] += 1
    maps[nowi][nowj][1] = top
    return maps

def mainloop():
    while 1:
        n = int(input())
        if not n:
            break
        # list comprehension imbriquée, style pythonic
        maps = [[[0,0] for _ in range(201)] for _ in range(201)]
        nowi = 100; nowj = 100
        entries = [tuple(map(int, input().split())) for _ in range(n)]
        for t, f in entries:
            maps = roll(maps, nowi, nowj, t, f)
        from collections import Counter
        flat = [maps[i][j][1] for i in range(201) for j in range(201) if maps[i][j][1]]
        cnt = Counter(flat)
        output = [str(cnt.get(i,0)) for i in range(1,7)]
        print(" ".join(output))
mainloop()