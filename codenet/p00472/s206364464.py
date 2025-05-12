n,m = map(int,input().split())
lng = [0]
for _ in range(n-1):
    lng.append(lng[-1] + int(input()))
i = 0
sm = 0
for _ in range(m):
    j = i+int(input())
    sm += abs(lng[i]-lng[j])
    sm %= 100000
    i = j
print(sm)