n, m = [int(x) for x in input().split()]
lng = [0]
for i in range(1, n):
    val = int(input())
    lng.append(lng[i-1] + val)

def abs_diff(a, b):
    return a - b if a >= b else b - a

i = 0
sm = 0
for _ in range(m):
    step = int(input())
    j = i + step
    sm += abs_diff(lng[i], lng[j])
    sm = sm % 100000
    i = j

print(sm)