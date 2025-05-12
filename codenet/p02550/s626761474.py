import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, X, M = map(int, input().split())
    L = [X]
    D = [0] * M
    D[X] = 1
    k = 2
    while k < N + 1:

        # k回目
        l = L[-1] ** 2 % M

        if D[l] != 0:
            n = N - k+1  # 残り回数
            one_cycle = k - D[l]
            mass = sum(L[D[l]-1:])
            ans = n//one_cycle *mass
            res = sum(L[D[l]-1:D[l]+(n%one_cycle)-1])
            print(ans +res +sum(L))
            exit()

        if l == 0:
            print(sum(L))
            exit()

        L.append(l)
        D[l] =k
        k += 1

    print(sum(L))

if __name__ == "__main__":
    main()

# \n