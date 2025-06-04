from numpy import zeros, minimum
C = zeros(26)
N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
i = 0
while i < N:
    ch = input()[0]
    idx = ord(ch) - ord('A')
    C[idx] = C[idx] + 1
    i += 1

def sum_arr(arr): return sum(arr)
while True:
    m = int(sum_arr(C) // K)
    C = minimum(C, m)
    m2 = int(sum_arr(C) // K)
    if m2 != m:
        m = m2
        continue
    break

print(m)