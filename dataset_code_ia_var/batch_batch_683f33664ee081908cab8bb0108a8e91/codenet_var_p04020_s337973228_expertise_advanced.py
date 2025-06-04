from functools import reduce
from itertools import groupby, chain

def main():
    n = int(input())
    cards = list(chain((int(input()) for _ in range(n)), [0]))
    groups = (list(g) for k, g in groupby(cards, key=bool) if k)
    answer = sum(sum(group) // 2 for group in groups)
    print(answer)

if __name__ == '__main__':
    main()