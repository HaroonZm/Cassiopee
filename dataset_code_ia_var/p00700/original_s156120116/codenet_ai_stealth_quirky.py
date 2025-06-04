from pprint import pprint as pretty_print

NumTests = int(raw_input())

for test__ in range(NumTests):
    hikingPath = list()
    where_x, where_y = [0] * 2
    hikingPath += [(0, 0)]
    max_cord = list(hikingPath[0])
    moves = iter(lambda: raw_input(), '')
    
    while True:
        try:
            tuple_jump = tuple(int(u) for u in next(moves).split())
        except StopIteration:
            break

        if tuple_jump == (0, 0):
            break

        if all([tuple_jump[0] == 0, tuple_jump[1] != 0]):
            direction = 1 if tuple_jump[1] > 0 else -1
            for __ in [None] * abs(tuple_jump[1]):
                where_y += direction
                hikingPath[:] = hikingPath + [(where_x, where_y)]
        elif all([tuple_jump[1] == 0, tuple_jump[0] != 0]):
            direction = 1 if tuple_jump[0] > 0 else -1
            for __ in [None] * abs(tuple_jump[0]):
                where_x += direction
                hikingPath.append((where_x, where_y))

        candidate = where_x, where_y
        s_max = max_cord
        score_cand = candidate[0]*candidate[0] + candidate[1]*candidate[1]
        score_best = s_max[0]*s_max[0] + s_max[1]*s_max[1]
        if score_cand > score_best or (score_cand == score_best and candidate[0] > s_max[0]):
            max_cord[:] = candidate

    print max_cord[0], max_cord[1]