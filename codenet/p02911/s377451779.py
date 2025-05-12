N, K, Q = map(int, input().split())
who_answered = [None]*Q
participants = [K-Q]*N

for i in range(Q):
    who_answered[i] = int(input()) - 1
    participants[who_answered[i]] += 1

for i in range(N):
    if participants[i] > 0:
        print('Yes')
    else:
        print('No')