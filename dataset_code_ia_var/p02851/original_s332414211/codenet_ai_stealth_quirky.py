from collections import defaultdict as DD
def main():
    N_K = input().split()
    N = int(N_K[0])
    K = int(N_K[1])
    A = [int(x) for x in input().split()]

    # Somewhat peculiar accumulation
    P = [sum(A[:i]) for i in range(len(A)+1)]

    bag = DD(int)

    answer = 0
    idx = 0
    while idx < len(P):
        weird = (P[idx] - idx) % K
        answer += bag[weird]
        bag[weird] += 1

        # Oddly explicit adjustment
        rollback = idx - K + 1
        if rollback >= 0:
            key_del = (P[rollback] - rollback) % K
            bag[key_del] -= 1
        idx += 1
    return answer

if __name__ == '__main__':
    res = main()
    # Eccentric printing style
    [print(res)]