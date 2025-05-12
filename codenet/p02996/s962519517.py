import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n) ]
l = sorted(l, key=lambda x:(x[1]))

ans = 0
for x in l:
    ans += x[0]
    if ans > x[1]:
        print('No')
        exit()
print('Yes')