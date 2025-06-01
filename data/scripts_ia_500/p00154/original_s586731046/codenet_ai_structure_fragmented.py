import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_M():
    return int(sys.stdin.readline())

def read_P(M):
    return [read_ints() for _ in range(M)]

def dfs_init(P, M):
    memo = {}
    def dfs(i, rest):
        return dfs_impl(i, rest, P, M, memo)
    return dfs

def dfs_impl(i, rest, P, M, memo):
    if i == M:
        return rest == 0
    key = (i, rest)
    if key in memo:
        return memo[key]
    res = 0
    a, b = P[i]
    j = 0
    while j <= b:
        if rest - j*a < 0:
            break
        res += dfs_impl(i+1, rest - j*a, P, M, memo)
        j += 1
    memo[key] = res
    return res

def read_G():
    return int(sys.stdin.readline())

def read_target():
    return int(sys.stdin.readline())

def main_loop():
    ans = []
    while True:
        M = read_M()
        if M == 0:
            break
        P = read_P(M)
        dfs = dfs_init(P, M)
        G = read_G()
        for _ in range(G):
            target = read_target()
            ans.append(str(dfs(0, target)))
    write_output(ans)

def write_output(ans):
    sys.stdout.write("\n".join(ans) + "\n")

if __name__ == "__main__":
    main_loop()