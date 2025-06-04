from functools import partial

def clamp(val, lo, hi):
    return max(lo, min(val, hi))

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    X = int(input())
    K = int(input())
    r = list(map(int, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # Differences between flip times
    sand_quantity = [r[0], *map(lambda ab: ab[1] - ab[0], zip(r, r[1:]))]

    s, e, y = 0, X, 0      # start, end, current sand
    sign = -1              # sand falling direction
    j = 0                  # pointer in r/sand_quantity
    chasm_time = 0

    clamp_ans = partial(clamp, lo=0, hi=X)
    for t, a in queries:
        # Step through all flips up to time t
        while j < K and r[j] < t:
            y += sign * sand_quantity[j]
            # s update
            if y < 0:
                s = min(e, s - y)
                y = 0
            # e update
            if X < y + e - s:
                diff = y + e - s - X
                e = max(s, e - diff)
            if X < y:
                y = X
            chasm_time = r[j]
            j += 1
            sign *= -1

        tmp_time = t - chasm_time

        if a < s:
            ret = y
        elif a < e:
            ret = y + a - s
        else:
            ret = y + e - s

        ret += tmp_time * sign
        print(clamp_ans(ret))