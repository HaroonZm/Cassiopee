N = int(input())
xor_sum = 0
for _ in range(N):
    w, b = map(int, input().split())
    xor_sum ^= (b - 1)
if xor_sum != 0:
    print(0)
else:
    print(1)