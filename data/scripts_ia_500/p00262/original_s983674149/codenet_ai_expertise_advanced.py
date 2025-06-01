from sys import stdin

for line in stdin:
    n = line.strip()
    if n == '0':
        break
    b = list(map(int, next(stdin).split()))
    count = 0
    target = list(range(1, len(b) + 1))
    while count < 10001:
        if b == target:
            print(count)
            break
        b = [x - 1 for x in b] + [len(b)]
        b = [x for x in b if x != 0]
        count += 1
    else:
        print(-1)