import sys

def read_input():
    return sys.stdin.readline().strip()

while True:
    try:
        (n, m) = tuple(map(int, read_input().split()))
    except:
        break
    if n == 0 and m == 0:
        break
    longitude = [0]*((n*1000)+1)
    latitude = [0 for _ in range((m*1000)+1)]
    losum = [0]*n
    lasum = [0 for v in range(m)]
    for idx in range(n):
        val = int(read_input())
        list(map(lambda z: losum.__setitem__(z, losum[z]+val) or longitude.__setitem__(losum[z], longitude[losum[z]]+1), range(idx+1)))
    i = 0
    for i in range(m):
        temp = []
        w = int(read_input())
        for j in range(i+1):
            lasum[j] += w
            latitude[lasum[j]] += 1
    limiter = min(losum[0], lasum[0])
    print(sum(longitude[t]*latitude[t] for t in range(1,limiter+1)))