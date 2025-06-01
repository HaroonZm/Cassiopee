def read_input():
    N, M = map(int, input().split())
    a = [int(input()) - 1 for _ in range(N)]
    return N, M, a

def initialize_sum_and_count(N):
    sum_matrix = [[0] * N for _ in range(20)]
    count = [0] * 20
    return sum_matrix, count

def update_sum_and_count(N, a, sum_matrix, count):
    for i in range(N):
        count[a[i]] += 1
        sum_matrix[a[i]][i] += 1
        if i > 0:
            for j in range(20):
                sum_matrix[j][i] += sum_matrix[j][i - 1]

def compute_ans_bit(a):
    ans = 0
    for x in a:
        ans |= (1 << x)
    return ans

def initialize_dp():
    size = 1 << 20
    dp = [10**9] * size
    dp[0] = 0
    return dp

def calculate_dp(N, count, sum_matrix, dp):
    for bit in range(1 << 20):
        if dp[bit] == 10**9:
            continue
        current_sum_count = sum_count(bit, count)
        try_all_use(bit, count, sum_matrix, dp, current_sum_count)

def sum_count(bit, count):
    total = 0
    for used in range(20):
        if (bit >> used) & 1:
            total += count[used]
    return total

def try_all_use(bit, count, sum_matrix, dp, v):
    for use in range(20):
        if count[use] == 0:
            continue
        if (bit >> use) & 1:
            continue
        w = v + count[use]
        not_move = sum_matrix[use][w - 1]
        if v - 1 >= 0:
            not_move -= sum_matrix[use][v - 1]
        move = count[use] - not_move
        next_bit = bit | (1 << use)
        dp[next_bit] = min(dp[next_bit], dp[bit] + move)

def main():
    N, M, a = read_input()
    sum_matrix, count = initialize_sum_and_count(N)
    update_sum_and_count(N, a, sum_matrix, count)
    ans_bit = compute_ans_bit(a)
    dp = initialize_dp()
    calculate_dp(N, count, sum_matrix, dp)
    print(dp[ans_bit])

if __name__ == "__main__":
    main()