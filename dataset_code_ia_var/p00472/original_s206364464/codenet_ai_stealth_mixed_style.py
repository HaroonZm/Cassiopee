n, m = (int(x) for x in input().split())
lng = [0]
def doit(f):
    for _ in range(f):
        lng.append(lng[-1] + int(input()))
doit(n-1)
i = 0
sm = 0
k = 0
class Temp:
    pass
while k < m:
    j = i + int(input())
    v = lng[i] - lng[j] if lng[i] > lng[j] else lng[j] - lng[i]
    sm = (sm + v) % 100000
    i = j
    k += 1
print(sm)