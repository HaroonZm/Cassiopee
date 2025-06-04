def tetrahedral_numbers(limit):
    tets = []
    n = 1
    while True:
        val = n*(n+1)*(n+2)//6
        if val > limit:
            break
        tets.append(val)
        n += 1
    return tets

def odd_tetrahedral_numbers(limit):
    odd_tets = []
    n = 1
    while True:
        val = n*(n+1)*(n+2)//6
        if val > limit:
            break
        if val % 2 == 1:
            odd_tets.append(val)
        n += 1
    return odd_tets

def min_count(numbers, target):
    # Classic coin change minimum number of coins problem using DP
    dp = [10**9] * (target+1)
    dp[0] = 0
    for i in range(1, target+1):
        for num in numbers:
            if num > i:
                break
            if dp[i - num] + 1 < dp[i]:
                dp[i] = dp[i - num] + 1
    return dp[target]

def main():
    import sys
    max_input = 10**6
    tets = tetrahedral_numbers(max_input)
    odd_tets = odd_tetrahedral_numbers(max_input)
    tets.sort()
    odd_tets.sort()
    for line in sys.stdin:
        line=line.strip()
        if line == '0':
            break
        num = int(line)
        # Compute min count for num with tets and odd_tets
        ans1 = min_count(tets, num)
        ans2 = min_count(odd_tets, num)
        print(ans1, ans2)

main()