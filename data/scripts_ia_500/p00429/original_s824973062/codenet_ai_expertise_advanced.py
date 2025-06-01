while True:
    n = int(input())
    if n == 0:
        break
    ar = input() + ' '
    for _ in range(n):
        ar = ''.join(f"{sum(1 for _ in group)}{char}" for char, group in __import__('itertools').groupby(ar))
    print(ar)