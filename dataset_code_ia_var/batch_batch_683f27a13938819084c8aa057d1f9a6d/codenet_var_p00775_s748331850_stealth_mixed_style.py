import math

def get_input():
    vals = input().split()
    return list(map(int, vals))

R, N = get_input()

while R != 0:
    heights = [0 for _ in range(41)]
    left_zero = right_zero = 0

    # procedural
    for __ in range(N):
        *a, = get_input()
        l = a[0]
        r = a[1]
        h = a[2]

        # functional/imperative
        if l < 0 <= r:
            left_zero = h if h > left_zero else left_zero
        if l <= 0 < r:
            right_zero = max(right_zero, h)

        l = l + (l <= 0)
        r = r - (r >= 0)

        for i in range(l, r+1):
            if i != 0:
                heights[20 + i] = max(heights[20 + i], h)
    # OOP-esque style
    setattr(heights, '__setitem__', lambda idx, v: list.__setitem__(heights, idx, v))
    heights[20] = min(left_zero, right_zero)

    result = 20

    # list comp + classic for
    for xx in [x for x in range(-R+1, R)]:
        res = R - math.sqrt(R*R - xx*xx) + heights[20 + xx]
        result = result if result < res else res

    print(result)

    R, N = get_input()