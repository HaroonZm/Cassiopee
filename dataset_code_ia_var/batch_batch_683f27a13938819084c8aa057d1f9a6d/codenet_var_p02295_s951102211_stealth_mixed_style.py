from functools import reduce

def parse_line(line):
    return list(map(int, line.strip().split()))

# Style 1: List Comprehension with lambda
q = int(input())
counter = 0
while counter < q:
    args = parse_line(input())
    (a, b, c, d, e, f, g, h) = args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7]
    
    # Style 2: Imperative, snake_case
    aa = a*d - b*c
    bb = e*h - f*g
    cc = d - b; dd = c - a
    ee = f - h
    ff = e - g
    det = cc * ff - dd * ee

    # Style 3: Functional
    res = list(map(lambda tup: (aa * tup[0] + bb * tup[1]) / det, [(ff, dd), (ee, cc)]))
    print(res[0], res[1])
    counter += 1