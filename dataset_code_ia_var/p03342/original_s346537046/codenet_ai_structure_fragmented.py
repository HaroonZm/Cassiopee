def read_input():
    return int(input()), list(map(int, input().split()))

def initialize_variables():
    return 0, 0, 0, 0

def is_valid(nowsum, nowxsum, A_r):
    return nowsum + A_r == (nowxsum ^ A_r)

def update_nowsum(nowsum, A_r):
    return nowsum + A_r

def update_nowxsum(nowxsum, A_r):
    return nowxsum ^ A_r

def revert_nowsum(nowsum, A_l):
    return nowsum - A_l

def revert_nowxsum(nowxsum, A_l):
    return nowxsum ^ A_l

def increase_r(r):
    return r + 1

def compute_increment(r, l):
    return r - l

def main():
    n, A = read_input()
    ans, l, r, nowsum = initialize_variables()
    nowxsum = 0
    for l in range(n):
        r = max(r, l)
        while r < n and is_valid(nowsum, nowxsum, A[r]):
            nowsum = update_nowsum(nowsum, A[r])
            nowxsum = update_nowxsum(nowxsum, A[r])
            r = increase_r(r)
        ans += compute_increment(r, l)
        nowsum = revert_nowsum(nowsum, A[l])
        nowxsum = revert_nowxsum(nowxsum, A[l])
    print(ans)

main()