# AOJ 0289: Infinite Express
# Python3 2018.6.23 bal4u

def calc(s, d):
    if s == d:
        return 0
    ans = 0
    if s & 1:
        ans += 1
        s += 1
    if d & 1:
        ans += 1
        d -= 1
    return ans + calc(s >> 1, d >> 1)

n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    print(calc(s, d))