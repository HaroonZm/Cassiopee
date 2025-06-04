def solve(X):
    ans = 0
    count = 0
    for c in X:
        if c == "S":
            count = count + 1
        else:
            if count > 0:
                count = count - 1
            else:
                ans = ans + 1
    ans = ans + count
    return ans

X = input()
result = solve(X)
print(result)