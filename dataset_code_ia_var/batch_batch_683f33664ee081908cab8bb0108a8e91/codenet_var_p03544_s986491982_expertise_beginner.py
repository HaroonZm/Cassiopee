def check(num, memo=None):
    if memo is None:
        memo = {}
    if num == 0:
        return 2
    elif num == 1:
        return 1
    elif num in memo:
        return memo[num]
    else:
        result = check(num - 1, memo) + check(num - 2, memo)
        memo[num] = result
        return result

n = input()
n = int(n)
print(check(n))