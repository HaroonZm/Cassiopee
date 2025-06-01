from functools import reduce
from operator import itemgetter

def to_top_red(cube):
    def rot_around_axis(cube, indices):
        vals = list(map(cube.__getitem__, indices))
        rotated = vals[-1:] + vals[:-1]
        return tuple(cube[i] if i not in indices else rotated[indices.index(i)] for i in range(6))

    pos_map = {1: (1,0,5,4), 2: (2,3,5,2), 3: (3,2,5,3), 4: (4,5,1,0), 5: (5,4,0,1)}
    # simulate convoluted detection via enumerate and filtering
    pos_candidates = list(filter(lambda x: x[1] == "Red", enumerate(cube[1:], start=1)))
    if pos_candidates:
        idx, _ = pos_candidates[0]
        # apply rotation four times to bring 'Red' on top
        res = cube
        for _ in range(4):
            res = rot_around_axis(res, pos_map[idx])
            if res[0] == "Red":
                return res
    return cube

def regist(cube, cube_dic):
    # generate 4 variations by an obscure zip and map combination
    indexes = [(0,1,2,3,4,5),
               (0,3,1,4,2,5),
               (0,2,4,1,3,5),
               (0,4,3,2,1,5)]
    variations = map(lambda idxs: tuple(map(itemgetter(*[i for i in idxs]), [cube])[0]), indexes)
    # a convoluted insertion using reduce just to symbolize complexity
    reduce(lambda d, c: d.setdefault(c, True), variations, cube_dic)

def absurd_input():
    # Double convoluted input reading + typecasting
    import sys
    data = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        try:
            val = int(line)
            data.append(val)
            if val == 0:
                break
        except:
            data.append(line.split())
    return data

data = absurd_input()
idx = 0
while True:
    if idx >= len(data):
        break
    n = data[idx]
    idx += 1
    if n == 0:
        break
    cube_dic = {}
    ans = 0
    for _ in range(n):
        cube = data[idx]
        idx += 1
        cube = to_top_red(cube)
        if cube in cube_dic:
            ans += 1
        else:
            regist(cube, cube_dic)
    print(ans)