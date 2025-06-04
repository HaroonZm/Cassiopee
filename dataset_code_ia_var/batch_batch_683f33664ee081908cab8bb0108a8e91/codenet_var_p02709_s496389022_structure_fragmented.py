def read_input():
    return int(input())

def read_array():
    return list(map(int, input().split()))

def enumerate_array(A):
    return [(a, i) for i, a in enumerate(A)]

def sort_array(arr):
    return sorted(arr, reverse=True)

def make_dp(N):
    return [0] * (N + 1)

def copy_dp(dp):
    return dp[:]

def update_left(dp2, l, dp, pos, a):
    dp2[l + 1] = max(dp2[l + 1], dp[l] + (pos - l) * a)

def update_right(dp2, l, dp, pos, a, N, i):
    r = i - l + 1
    dp2[l] = max(dp2[l], dp[l] + (N - r - pos) * a)

def process_dp(N, A):
    dp = make_dp(N)
    for i in range(N):
        dp2 = copy_dp(dp)
        for l in range(i + 1):
            a, pos = A[i]
            update_left(dp2, l, dp, pos, a)
            update_right(dp2, l, dp, pos, a, N, i)
        dp = dp2
    return dp

def get_result(dp):
    return max(dp)

def main():
    N = read_input()
    arr = read_array()
    arr_enum = enumerate_array(arr)
    arr_sorted = sort_array(arr_enum)
    dp = process_dp(N, arr_sorted)
    result = get_result(dp)
    print(result)

main()