n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def apply_Q(seq):
    return [Q[x-1] for x in seq]

max_day = 10**18
current = P[:]
for day in range(max_day+1):
    if all(current[i] == i+1 for i in range(n)):
        print(day)
        break
    current = apply_Q(current)
else:
    print(-1)