from sys import stdin

s = stdin.readline().rstrip()
n = int(stdin.readline())

ops = [stdin.readline().split() for _ in range(n)]

for op in ops:
    cmd, a, b, *rest = op
    a, b = int(a), int(b)
    substr = s[a:b+1]
    match cmd:
        case 'replace':
            s = f"{s[:a]}{rest[0]}{s[b+1:]}"
        case 'reverse':
            s = f"{s[:a]}{substr[::-1]}{s[b+1:]}"
        case 'print':
            print(substr)