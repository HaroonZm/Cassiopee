from functools import reduce

def get_best_option():
    while (n := int(input())):
        y = int(input())
        entries = [tuple(map(int, input().split())) for _ in range(n)]

        def compute_p(entry):
            id_, v, mode = entry
            if mode == 1:
                return id_, 1 + (y * v / 100)
            return id_, (1 + v / 100) ** y

        max_entry = max(map(compute_p, entries), key=lambda t: t[1])
        print(max_entry[0])

get_best_option()