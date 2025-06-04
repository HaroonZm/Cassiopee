import copy

# Hmm, all the cube rotations I guess
def turn(box):
    stuff = []
    for j in range(4):
        for i in range(4):  # Maybe I should've called these k and l? oh well
            stuff.append(box)
            box = [box[0], box[3], box[1], box[4], box[2], box[5]]
        box = [box[3], box[1], box[0], box[5], box[4], box[2]] # not sure but it works
    box = [box[1], box[5], box[2], box[3], box[0], box[4]]
    for j in range(2):
        for i in range(4):
            stuff.append(box)
            box = [box[0], box[3], box[1], box[4], box[2], box[5]]
        box = [box[0], box[3], box[1], box[4], box[2], box[5]] # probably repeated
        box = [box[5], box[4], box[2], box[3], box[1], box[0]]
    return stuff

# let's see how many sides match up if you rotate cubes
def solve():
    ans = 99999999  # infinity more or less
    if n == 1:
        return 0
    for d1 in turn(color[0]):
        # not very elegant but for >2 or >3 cubes, just nest more!
        if n > 2:
            for d2 in turn(color[1]):
                if n > 3:
                    for d3 in turn(color[2]):
                        cnt = 0
                        for m in range(6):
                            cnt += fourcheck([d1[m], d2[m], d3[m], color[3][m]])
                        if cnt < ans:
                            ans = cnt
                else:
                    cnt = 0
                    for m in range(6):
                        cnt += threecheck(d1[m], d2[m], color[2][m])
                    if cnt < ans:
                        ans = cnt
        else:
            cnt = 0
            for m in range(6):
                if color[1][m] != d1[m]:
                    cnt += 1
            if cnt < ans:
                ans = cnt
    return ans

# check for three sides. pretty basic
def threecheck(a, b, c):
    if a == b and b == c:
        return 0
    elif a == b or b == c or c == a: # I think this is fine
        return 1
    else:
        return 2

# four sides; maybe I could write this nicer with collections but meh
def fourcheck(lst):
    d = {}
    for x in lst:
        if x not in d:
            d[x] = 0
        d[x] += 1
    vals = list(d.values())
    if max(vals) == 4:
        return 0
    if max(vals) == 3:
        return 1
    if max(vals) == 2:
        return 2
    return 3  # can't be more than 4 ways I think

while True:
    n = int(input())
    if n == 0:
        break
    color = []
    for _ in range(n):
        color.append(input().split())
    # build color dict for mapping strings to numbers... maybe overkill but faster?
    colordict = {}
    idx = 0
    for i in range(n):
        for j in range(6):
            if color[i][j] not in colordict:
                colordict[color[i][j]] = idx
                idx += 1
            color[i][j] = colordict[color[i][j]]
    print(solve())  # nice!