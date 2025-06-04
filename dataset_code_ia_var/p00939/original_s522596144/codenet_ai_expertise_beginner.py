def solve():
    D = input()
    n = len(D)
    digits = []
    for ch in D:
        digits.append(int(ch))
    total_sum = 0
    for x in digits:
        total_sum += x
    total_product = 1
    for ch in D:
        total_product *= int(ch) + 1

    # memoization for dfs0
    memo = []
    for i in range(n):
        memo.append({})

    def dfs0(idx, s, p):
        key = (s, p)
        if idx == n:
            if s > 0:
                return 1
            if s == 0 and p < total_product:
                return 1
            return 0
        if key in memo[idx]:
            return memo[idx][key]
        result = 0
        max_digit = min(s, 9)
        for v in range(0, max_digit + 1):
            result += dfs0(idx + 1, s - v, p * (v + 1))
        memo[idx][key] = result
        return result

    res1 = dfs0(0, total_sum, 1)

    # memoization for dfs1
    memo1 = []
    for i in range(n):
        memo1.append({})

    def dfs1(idx, s, p, m):
        key = (s, p, m)
        if idx == n:
            if s == 0 and p == 1:
                return 1
            return 0
        if key in memo1[idx]:
            return memo1[idx][key]
        result = 0
        min_value = s - (n - 1 - idx) * 9
        digi = digits[idx]
        # Make sure min_value is not negative
        if min_value < 0:
            min_value = 0
        max_v = min(s, 9)
        for v in range(min_value, max_v + 1):
            if p % (v + 1) != 0:
                continue
            if m == 0:
                if digi < v:
                    break
                if v < digi:
                    next_m = 1
                else:
                    next_m = 0
                result += dfs1(idx + 1, s - v, p // (v + 1), next_m)
            else:
                result += dfs1(idx + 1, s - v, p // (v + 1), 1)
        memo1[idx][key] = result
        return result

    res2 = dfs1(0, total_sum, total_product, 0) - 1

    answer = res1 + res2
    print(answer)

solve()