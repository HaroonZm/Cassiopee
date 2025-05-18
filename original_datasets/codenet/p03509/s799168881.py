N, P = map(int, input().split())
B = 0
Q = []
for i in range(N):
    w, b = map(int, input().split())
    B += b
    Q.append((100 - P)*w + P*b)
Q.sort()
s = 0
for i in range(N):
    s += Q[-i-1]
    if B*P <= s:
        print(i+1)
        break