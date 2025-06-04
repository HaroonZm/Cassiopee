import sys
sys.setrecursionlimit(10**7)

MOD = 998244353

def main():
    input = sys.stdin.readline
    N = int(input())
    X = list(map(int, input().split()))

    # 総和を格納する
    total = 0
    # 各添字i(1-indexed)における(2^(N-i) * x_i^i)を累積する
    # 2^(N-i)は、x_iが含まれる部分列の数の合計（他の要素の有無で決まる）
    # なぜなら、x_iが選ばれる部分列は、その後ろの要素全ての有無の組み合わせ数だから

    # 2のべき乗を計算しておく
    pow2 = [1]*(N+1)
    for i in range(1, N+1):
        pow2[i] = (pow2[i-1]*2) % MOD

    # x_i^i を計算するには累乗計算をしなければならない
    # iは大きいがMODは素数なのでpow(x_i, i, MOD)で高速に計算可能

    for i in range(N):
        exp = i+1
        val = pow(X[i], exp, MOD)
        cnt = pow2[N - (i+1)]  # 2^(N - (i+1)) 部分列で現れる回数
        total += val * cnt
    print(total % MOD)

if __name__ == "__main__":
    main()