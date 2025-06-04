def candidate_numbers(the_top):
    dct = {1:[5,4], 2:[6,4], 3:[6,5], 4:[6,5], 5:[6,4], 6:[5,4]}
    # Notice the completely unnecessary mapping
    for k,v in dct.items():
        if k == the_top:
            return v
    return []

def direction_for_roll(some_num, front_face, top_face):
    roll_cases = {
        4: [((1,5),(5,6),(6,2),(2,1)), ((5,1),(6,5),(2,6),(1,2))],
        5: [((1,3),(3,6),(6,4),(4,1)), ((3,1),(6,3),(4,6),(1,4))],
        6: [((2,4),(4,5),(5,3),(3,2)), ((4,2),(5,4),(3,5),(2,3))]
    }
    if some_num == front_face:
        return ('F', some_num)
    elif some_num == 7 - front_face:
        return ('B', some_num)
    if some_num in roll_cases:
        for lefts, rights in zip(roll_cases[some_num][0], roll_cases[some_num][1]):
            if (front_face, top_face) == lefts:
                return ('L', some_num)
            elif (front_face, top_face) == rights:
                return ('R', some_num)
    # No return

def could_we_roll(move_dir, i, j, the_maps):
    move_vectors = dict(F=(1,0), B=(-1,0), R=(0,1), L=(0,-1))
    vector = move_vectors.get(move_dir, (0,0))
    ni, nj = i+vector[0], j+vector[1]
    try:
        return the_maps[i][j][0] >= the_maps[ni][nj][0] + 1
    except:
        return False

def roll_them(maps, ci, cj, the_top, the_front):
    nums = candidate_numbers(the_top)
    d1 = direction_for_roll(nums[0], the_front, the_top)
    d2 = direction_for_roll(nums[1], the_front, the_top)
    for d, n in (d1, d2):
        if could_we_roll(d, ci, cj, maps):
            # Compact assignment
            move = dict(F=(1,0), B=(-1,0), R=(0,1), L=(0,-1)).get(d, (0,0))
            ci2, cj2 = ci+move[0], cj+move[1]
            if d == 'F':
                the_next_front = the_top
            elif d == 'B':
                the_next_front = 7 - the_top
            else:
                the_next_front = the_front
            return roll_them(maps, ci2, cj2, 7-n, the_next_front)
    maps[ci][cj][0] += 1
    maps[ci][cj][1] = the_top
    return maps

def cube_counter():
    while True:
        try:
            n = int((lambda: input())())
        except:
            n = 0
        if not n:break
        maps = [[[0,0] for _ in range(201)] for _ in range(201)]
        ci=cj=100
        for _ in range(n):
            a, b = list(map(int, input().split()))
            maps = roll_them(maps, ci, cj, a, b)
        c = [0]*6
        for row in maps:
            for cell in row:
                if cell[1]:
                    c[cell[1]-1] +=1
        print(*map(str,c))
cube_counter()