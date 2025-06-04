from functools import cache

def main():
    n, a, b, c = map(int, input().split())
    l_list = [int(input()) for _ in range(n)]

    @cache
    def dfs(i, a_sum, b_sum, c_sum):
        if i == n:
            if min(a_sum, b_sum, c_sum) == 0:
                return float('inf')
            return abs(a - a_sum) + abs(b - b_sum) + abs(c - c_sum) - 30
        l = l_list[i]
        skip = dfs(i + 1, a_sum, b_sum, c_sum)
        use_a = dfs(i + 1, a_sum + l, b_sum, c_sum) + 10
        use_b = dfs(i + 1, a_sum, b_sum + l, c_sum) + 10
        use_c = dfs(i + 1, a_sum, b_sum, c_sum + l) + 10
        return min(skip, use_a, use_b, use_c)

    print(dfs(0, 0, 0, 0))

if __name__ == "__main__":
    main()