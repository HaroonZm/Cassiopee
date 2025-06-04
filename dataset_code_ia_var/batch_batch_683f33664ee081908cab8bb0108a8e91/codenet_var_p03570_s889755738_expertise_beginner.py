s = input()

alp = "abcdefghijklmnopqrstuvwxyz"
alpdic = {}
for i in range(26):
    alpdic[alp[i]] = i

memo = {}
bit = 0
memo[bit] = 0

for c in s:
    idx = alpdic[c]
    bit = bit ^ (1 << idx)

    ans = 9999999
    if bit in memo:
        ans = memo[bit]

    for i in range(26):
        test_bit = bit ^ (1 << i)
        if test_bit in memo:
            ans = min(ans, memo[test_bit])

    if bit in memo:
        memo[bit] = min(memo[bit], ans + 1)
    else:
        memo[bit] = ans + 1

print(max(1, memo[bit]))