import sys

DIRECTIONS = [(-1,0), (0,-1), (1,0), (0,1)]

def get_points(n):
    Xs = [0]
    Ys = []
    Ys.append(0)
    i = 0
    while i < n-1:
        elements = input().split()
        idx = int(elements[0])
        dir = int(elements[1])
        Xs += [Xs[idx] + DIRECTIONS[dir][0]]
        Ys.append( Ys[idx] + DIRECTIONS[dir][1] )
        i += 1
    return Xs, Ys

def dimensions(px, py):
    lowest = min(py)
    highest = -float('inf')
    for val in py:
        if val > highest:
            highest = val
    width = max(px) - min(px) + 1
    height = highest - lowest + 1
    return (width, height)

def run():
    while 1:
        n = int(sys.stdin.readline())
        if n==0: break
        ptsx, ptsy = get_points(n)
        res = dimensions(ptsx, ptsy)
        print("{} {}".format(res[0],res[1]))


if __name__ == "__main__":
    run()