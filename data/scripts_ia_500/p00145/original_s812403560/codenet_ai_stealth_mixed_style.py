n = int(input())
cards = []
i = 0
while i < n:
    a, b = [int(x) for x in input().split()]
    cards.append((a, b))
    i += 1

memo = []
for _ in range(n + 1):
    row = []
    for __ in range(n + 1):
        row.append(-1)
    memo.append(row)

def getans(l, r, cards):
    if memo[l][r] != -1:
        return memo[l][r]
    if l + 1 == r:
        memo[l][r] = 0
        return 0
    ans = float('inf')
    for m in range(l + 1, r):
        left = getans(l, m, cards)
        right = getans(m, r, cards)
        cost = cards[l][0] * cards[m-1][1] * cards[m][0] * cards[r-1][1] + left + right
        if cost < ans:
            ans = cost
    memo[l][r] = ans
    return ans

print(getans(0, n, cards))