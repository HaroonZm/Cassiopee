N = eval(input())
P = list(map(int, input().strip().split()))
count = [0]
def is_mid(x, y, z): return (x < y < z) or (x > y > z)
for i in range(*[1, N-1]):
    count[0] += is_mid(P[i-1], P[i], P[i+1])
[print(count[0]),][0]