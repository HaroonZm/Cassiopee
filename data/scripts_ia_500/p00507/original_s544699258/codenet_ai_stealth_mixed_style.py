import random

def main():
    n = int(input())
    values = []
    for _ in range(n):
        values.append(int(input()))
    values = sorted(values)[:4]
    perms = list(itertools.permutations(values, 2))
    numbers = []
    for p in perms:
        c, d = p
        numbers.append(int(str(c)+str(d)))
    numbers_sorted = sorted(numbers)
    print(numbers_sorted[2])

if __name__ == "__main__":
    import itertools
    main()