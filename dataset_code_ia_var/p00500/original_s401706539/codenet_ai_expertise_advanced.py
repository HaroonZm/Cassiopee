from itertools import starmap

def check(arr, n):
    seen = set()
    for idx, val in enumerate(arr[:n]):
        if val and val not in seen:
            seen.add(val)
        elif val:
            arr[idx] = 0
            first_idx = arr.index(val)
            arr[first_idx] = 0

if __name__ == '__main__':
    n = int(input())
    rows = [tuple(map(int, input().split())) for _ in range(n)]
    a, b, c = zip(*rows)
    a, b, c = list(a), list(b), list(c)
    for lst in (a, b, c):
        check(lst, n)
    print(*starmap(lambda x, y, z: x + y + z, zip(a, b, c)), sep='\n')