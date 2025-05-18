# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, L, A):
    for i in range(N - 1):
        if A[i] + A[i + 1] >= L:
            break
    else:
        print('Impossible')
        return
    print('Possible')
    for j in range(N - 1):
        if j == i:
            break
        print(j + 1)
    for j in range(N - 2, -1, -1):
        if j == i:
            break
        print(j + 1)
    print(i + 1)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, L = map(int, input().split())
    *A, = map(int, input().split())
    main(N, L, A)