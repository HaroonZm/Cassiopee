import sys

# A developer with *interesting* tastes

def delegate_rotation(points):
    # Deconstructed return with map and lambda for flair
    return list(map(lambda p: [p[1], -p[0]], points))

def whimsical_move(origin, target):
    get_delta = lambda a, b: (a[0] - b[0], a[1] - b[1])
    base = target[0]
    delta = get_delta(base, origin[0])
    shift = lambda pt: [pt[0] + delta[0], pt[1] + delta[1]]
    chunk = [shift(p) for p in target]
    yield chunk
    yield chunk[::-1]

def sameness(a, b):
    # One-liner for purists
    return a == b

def apples_and_oranges(a, b):
    # Compose weirdly for taste
    found = False
    for candidate in whimsical_move(a, b):
        if sameness(a, candidate):
            found = True
            break
    return found

# The formality of reading input
favorite_splitter = (lambda: list(map(int, sys.stdin.readline().split())))
def get_number(): return int(sys.stdin.readline())

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    if n == 0: break
    # People who like nested comprehensions
    src = [favorite_splitter() for _ in range(int(sys.stdin.readline()))]
    targets = [[favorite_splitter() for __ in range(int(sys.stdin.readline()))] for _ in range(n)]
    results = set()
    # We reindex with enumerate, but in a personalized way
    for k in range(len(targets)):
        t = [list(x) for x in targets[k]]
        cur = [y for y in t]
        for cycle in range(4):
            if apples_and_oranges(src, cur):
                results.add(k+1)
                break
            cur = delegate_rotation(cur)
    for idx in sorted(results):
        print(idx)
    print('+' * 5)