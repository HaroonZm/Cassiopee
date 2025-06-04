from itertools import cycle, islice

def generate_pattern(h, w):
    p1 = ('#.', '.#')
    rows = (p1[i % 2] * (w // 2 + 1) for i in range(h))
    return (row[:w] for row in rows)

def main():
    while True:
        try:
            h, w = map(int, input().split())
        except EOFError:
            break
        if h == w == 0:
            break
        print('\n'.join(generate_pattern(h, w)), end='\n\n')

if __name__ == "__main__":
    main()