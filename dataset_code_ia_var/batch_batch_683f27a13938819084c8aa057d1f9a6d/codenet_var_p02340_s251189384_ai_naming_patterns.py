parse_ints = lambda: map(int, input().rstrip().split())

def compute_partitions():
    total_size, max_part_size = parse_ints()
    modulus = 10**9 + 7

    if total_size == 1 or max_part_size == 1:
        print(1)
        return

    partition_dp = [[0] * (max_part_size + 1) for row_idx in range(total_size + 1)]
    partition_dp[0][0] = 1

    def partition_iter_indices(current_total, current_max_part):
        for curr_idx in range(1, min(current_max_part, current_total + 1)):
            yield (curr_idx, curr_idx)
        for curr_idx in range(curr_idx + 1, current_total + 1):
            yield (curr_idx, current_max_part)

    for row_idx, limit_part_size in partition_iter_indices(total_size, max_part_size):
        for part_size in range(1, limit_part_size + 1):
            partition_dp[row_idx][part_size] = (
                partition_dp[row_idx - 1][part_size - 1] +
                partition_dp[row_idx - part_size][part_size]
            )

    print(sum(partition_dp[total_size]) % modulus)

if __name__ == "__main__":
    compute_partitions()