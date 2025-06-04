from sys import stdin
from bisect import bisect_left, bisect_right

def get_subsets_sums(arr):
    n = len(arr)
    subsets = [[] for _ in range(n+1)]
    # subsets[k] will hold sums of all subsets of size k
    def dfs(i, count, total):
        if i == n:
            subsets[count].append(total)
            return
        # take arr[i]
        dfs(i+1, count+1, total + arr[i])
        # don't take arr[i]
        dfs(i+1, count, total)
    dfs(0, 0, 0)
    return subsets

def main():
    input = stdin.read().strip().split()
    N, K, L, R = map(int, input[0:4])
    coins = list(map(int, input[4:]))

    left_part = coins[:N//2]
    right_part = coins[N//2:]

    left_sums = get_subsets_sums(left_part)
    right_sums = get_subsets_sums(right_part)

    # sort each list in right_sums for binary search
    for lst in right_sums:
        lst.sort()

    result = 0
    # For each number of coins chosen in left part, choose complementary in right part
    for left_k in range(max(0, K - len(right_part)), min(K, len(left_part)) + 1):
        right_k = K - left_k
        left_list = left_sums[left_k]
        right_list = right_sums[right_k]
        # For each sum in left_list, find how many in right_list to fall in [L - sum, R - sum]
        for s in left_list:
            low = L - s
            high = R - s
            left_index = bisect_left(right_list, low)
            right_index = bisect_right(right_list, high)
            result += (right_index - left_index)

    print(result)

if __name__ == "__main__":
    main()