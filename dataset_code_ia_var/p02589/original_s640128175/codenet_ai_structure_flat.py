import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

N = int(readline())
S = np.array(list(read().rstrip()), np.int64)
S[S == ord('\n')] = -1
S[S > 0] -= ord('a')
S = np.insert(S, 0, -1)
S = np.append(S, -1)

S = S.copy()
w = np.where(S == -1)[0]
l_ind = w[:-1] + 1
r_ind = w[1:]

N_range = len(l_ind)
ii = 0
while ii < N_range:
    la = l_ind[ii]
    ra = r_ind[ii]
    S[la:ra] = S[la:ra][::-1]
    ii += 1

path = np.zeros_like(S)
child = np.zeros((len(S), 26), np.int64)
is_end = np.zeros(len(S), np.bool_)

n_node = 1
i = 0
while i < N_range:
    node = 0
    j = l_ind[i]
    while j < r_ind[i]:
        path[j] = node
        if child[node][S[j]] == 0:
            child[node][S[j]] = n_node
            n_node += 1
        node = child[node][S[j]]
        j += 1
    is_end[node] = True
    i += 1

child = child[:n_node]
is_end = is_end[:n_node]
ans = 0
i = 0
while i < N_range:
    se = 0
    j = r_ind[i] - 1
    while j >= l_ind[i]:
        se |= 1 << S[j]
        node = path[j]
        k = 0
        while k < 26:
            if se & (1 << k):
                if child[node][k] < len(is_end) and is_end[child[node][k]]:
                    ans += 1
            k += 1
        j -= 1
    i += 1

print(ans - N_range)