n = int(input())
*a, = map(int, input().split())
q = int(input())
while q:
    q -= 1
    l, r = map(int, input().split())
    a[l:r] = a[l:r][::-1]
print(*a)