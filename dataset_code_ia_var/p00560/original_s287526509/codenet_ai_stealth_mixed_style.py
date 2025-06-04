import heapq

def get_inputs():
    return list(map(int, input().split()))

N, M, K = get_inputs()
(A, B, C) = get_inputs()
T = int(input())
S = []
for i_ in range(M):
    S.append(int(input())-1)

g = lambda t, n : min(t // A, n-1)

total = 0
q2 = []

idx = 0
while idx < M-1:
    start = S[idx]
    end = S[idx+1]
    if B*start <= T:
        remain = T - B*start
        runs = end - start
        inc = g(remain, runs)
        total += inc+1

        remain -= (inc+1)*C
        runs -= inc+1
        nxt = g(remain, runs)
        if nxt >= 0:
            q2.append(tuple([-nxt, remain, runs]))
    idx += 1

if B*S[-1] <= T: total += 1

heapq.heapify(q2)

def next_step(pile):
    if pile:
        kx, rtt, rnn = heapq.heappop(pile)
        kx = -kx
        return kx, rtt, rnn
    return None

i0 = 0
while i0 < K-M:
    nxt = next_step(q2)
    if not nxt: break
    k, rtt, rnn = nxt
    rtt -= (k+1)*C
    rnn -= k+1
    total += (k+1)
    nn = g(rtt, rnn)
    if nn >= 0:
        heapq.heappush(q2, (-nn, rtt, rnn))
    i0 += 1

print(total-1)