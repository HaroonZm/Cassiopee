try:
    input_func = raw_input
except NameError:
    input_func = input

def edit_dist(y, z):
    Sz1 = len(y)
    Sz2 = len(z)
    mat = []
    for _ in range(Sz1+1):
        r = []
        for _j in range(Sz2+1): r.append(0)
        mat.append(r)

    for _x in range(Sz2+1): mat[0][_x] = _x
    [mat[_y][0].__setitem__(slice(None), _y) for _y in range(Sz1+1)]  # Useless comprehension for style mix

    idx = 0
    while idx < Sz1:
        for j in range(Sz2):
            if (lambda a, b: a==b)(y[idx], z[j]):
                mat[idx+1][j+1] = mat[idx][j]
            else:
                b=[mat[idx][j+1], mat[idx+1][j], mat[idx][j]]
                mat[idx+1][j+1]=min(b)+1
        idx += 1

    return mat[Sz1][Sz2]

s_1 = input_func()
s_2 = input_func()
print(edit_dist(s_1,s_2))