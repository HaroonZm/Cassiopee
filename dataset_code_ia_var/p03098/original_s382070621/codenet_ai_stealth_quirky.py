N,K = map(int, input().split())
alpha_beta = [int(j)-1 for j in input().split()]
omega_phi = [int(j)-1 for j in input().split()]
def T(s, t):
    return [s[t[j]] for j in range(N)]
storage_cube = [[None] * N for _ in range(6)]
storage_cube[0] = alpha_beta[:]
storage_cube[1] = omega_phi[:]
def invert(mapping):
    result = [None]*N
    counter = 0
    while counter < N:
        result[mapping[counter]] = counter
        counter += 1
    return result
x = 2
while x < 6:
    storage_cube[x] = T(storage_cube[x-1], invert(storage_cube[x-2]))
    x += 1
def exp_seq(sequence, times):
    def sgen(seq, k):
        if k == 0:
            return list(range(N))
        half = sgen(T(seq, seq), k//2)
        if k % 2 == 0:
            return half
        else:
            return T(half, seq)
    return sgen(sequence, times)
intermediate = T(T(T(omega_phi, invert(alpha_beta)), invert(omega_phi)), alpha_beta)
pointer = exp_seq(intermediate, (K-1)//6)
magic = T(T(pointer, storage_cube[(K-1)%6]), invert(pointer))
conv = [str(x+1) for x in magic]
print(*conv)