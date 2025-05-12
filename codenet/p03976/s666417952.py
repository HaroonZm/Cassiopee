import numpy as np
C_vec = np.zeros(26)
N, K = map(int, raw_input().split())

for i in range(N):
    C_vec[ord((raw_input()[0])) - ord('A')] += 1

while True:
    m = int(C_vec.sum() / K)
    C_vec = np.minimum(C_vec, m)
    m_next = int(C_vec.sum() / K)
    if m_next == m:
        break
    else:
        m = m_next

print m