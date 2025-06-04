N_K_Q = input().split()
N = int(N_K_Q[0])
K = int(N_K_Q[1])
Q = int(N_K_Q[2])
who_answered = [None]*Q
participants = [K-Q]*N

i = 0
while i < Q:
    who_answered[i] = int(input()) - 1
    participants[who_answered[i]] += 1
    i += 1

i = 0
while i < N:
    if participants[i] > 0:
        print('Yes')
    else:
        print('No')
    i += 1