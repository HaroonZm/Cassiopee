q, h, s, d = map(int, input().split())
n = int(input())

l1, l2 = min(q*4, h*2, s), min(q*8, h*4, s*2, d)
if n % 2 == 0:
    print(l2 * (n//2))
else:
    print(l2 * (n//2) + l1)