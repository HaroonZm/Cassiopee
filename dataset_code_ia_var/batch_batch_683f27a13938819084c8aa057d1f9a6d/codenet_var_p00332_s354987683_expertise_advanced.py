from functools import partial

def solve(e, y):
    eras = [
        (1868, 1912, 'M'),
        (1912, 1926, 'T'),
        (1926, 1989, 'S'),
        (1989, float('inf'), 'H')
    ]
    if e == 0:
        r = next(f"{symbol}{y-start+1}" for start, end, symbol in eras if start <= y < end)
    else:
        starts = [0, 1868, 1912, 1926, 1989]
        r = starts[e] + y - 1
    return r

def main():
    E, Y = map(int, input().split())
    print(solve(E, Y))

if __name__ == '__main__':
    main()