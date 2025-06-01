def update_counts_forward(i, c, a0_a1_a2):
    a0, a1, a2 = a0_a1_a2
    if c == 'J':
        a0 += 1
    elif c == 'O':
        a1 += a0
    else:
        a2 += a1
    return a0, a1, a2

def compute_prefix_counts(S, N):
    a0 = 0
    a1 = 0
    a2 = 0
    P = [0]*N
    for i, c in enumerate(S):
        a0, a1, a2 = update_counts_forward(i, c, (a0, a1, a2))
        P[i] = a0
    return P, a1, a2

def update_counts_backward(i, c, b0_b1_b2):
    b0, b1, b2 = b0_b1_b2
    if c == 'I':
        b0 += 1
    elif c == 'O':
        b1 += b0
    else:
        b2 += b1
    return b0, b1, b2

def compute_suffix_counts(S, N):
    b0 = 0
    b1 = 0
    b2 = 0
    Q = [0]*N
    for i, c in enumerate(reversed(S)):
        b0, b1, b2 = update_counts_backward(i, c, (b0, b1, b2))
        Q[-1 - i] = b0
    return Q, b1, b2

def compute_result_max(P, Q, a1, b1, a2, N):
    res = max(a1, b1)
    for i in range(N):
        res = max(res, P[i] * Q[i])
    return res + a2

def main():
    N = int(input())
    S = input()
    P, a1, a2 = compute_prefix_counts(S, N)
    Q, b1, b2 = compute_suffix_counts(S, N)
    result = compute_result_max(P, Q, a1, b1, a2, N)
    print(result)

main()