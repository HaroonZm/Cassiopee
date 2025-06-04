from itertools import product, islice

def main(h, w):
    a = h * h + w * w
    candidates = ((x ** 2 + y ** 2, x, y)
                  for x, y in product(range(1, 151), repeat=2) if x < y and a <= x ** 2 + y ** 2)
    b, x, y = min(candidates, key=lambda t: (t[0], t[1]))  # pick lex smallest
    print(x, y)

while True:
    try:
        h, w = map(int, input().split())
        if not (h or w):
            break
        main(h, w)
    except EOFError:
        break