import sys

def read_int():
    return int(sys.stdin.readline())

def main():
    N = int(sys.stdin.readline())
    A = []
    for i in range(N):
        A.append(int(sys.stdin.readline()))
    A.sort()
    l1 = []
    u1 = []
    l2 = []
    u2 = []
    for i in range(N):
        if i < N // 2:
            l1.append(A[i])
        else:
            u1.append(A[i])
        if i < (N + 1) // 2:
            l2.append(A[i])
        else:
            u2.append(A[i])
    if N % 2 == 1:
        sum_u1 = sum(u1)
        sum_l1 = sum(l1)
        ans1 = (2 * sum_u1 - u1[0] - u1[1]) - 2 * sum_l1

        sum_u2 = sum(u2)
        sum_l2 = sum(l2)
        ans2 = 2 * sum_u2 - (2 * sum_l2 - l2[-1] - l2[-2])

        ans = max(ans1, ans2)
    else:
        sum_u1 = sum(u1)
        sum_l1 = sum(l1)
        ans = (2 * sum_u1 - u1[0]) - (2 * sum_l1 - l1[-1])
    print(ans)

if __name__ == "__main__":
    main()