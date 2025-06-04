from collections import Counter
from sys import exit

h, w = map(int, input().split())
grid = [ch for _ in range(h) for ch in input()]
cnt = Counter(grid)

four = (h // 2) * (w // 2)
two = (h % 2) * (w // 2) + (w % 2) * (h // 2)
one = (h % 2) * (w % 2)

for val in cnt.values():
    q4, rem = divmod(val, 4)
    use4 = min(q4, four)
    four -= use4
    rem += 4 * (q4 - use4)

    q2, rem = divmod(rem, 2)
    if q2 > two:
        print("No")
        exit()
    two -= q2

    if rem:
        if one == 0:
            print("No")
            exit()
        one -= 1

print("Yes" if four == two == one == 0 else "No")