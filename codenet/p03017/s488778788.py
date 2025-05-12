def iwa_check(start, end):
    for i in range(start, end):
        if s[i] == '#' and s[i + 1] == '#':
            return False
    return True

n, a, b, c, d = map(int, input().split())
s = list(input())
s = ['#'] + s + ['#']

# 岩が2個並ぶ
if not iwa_check(a, c) or not iwa_check(b, d):
    print('No')
    exit()

# 追い越す場合
if c > d:
    ok = False
    for i in range(b, d + 1):
        if s[i - 1] == '.' and s[i] == '.' and s[i + 1] == '.':
            ok = True
            break
    if not ok:
        print('No')
        exit()

# 追い越さない
print('Yes')