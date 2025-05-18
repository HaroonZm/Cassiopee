# https://pitsbuffersolution.com/compro/atcoder/arc079e.php

def main():
    N = int(input())
    *a, = map(int, input().split())

    tot = sum(a)

    def is_ok(k):
        b = (x + k - (N - 1) for x in a)

        cnt = 0
        for x in b:
            cnt += (x + N) // (N + 1)

        return cnt <= k

    ret = 0

    k = max(0, tot - N * (N - 1))
    while k <= tot:
        if is_ok(k):
            ret = k
            break
        k += 1

    print(ret)

if __name__ == '__main__':
    main()