a, n, m = map(int, input().split())
candi = []
ans = 0

for i in range(a + 1, 9*8+a+1):
    if i**n <= m:
        candi.append(i**n)
for j in candi:
    k = j
    digit = []
    for _ in range(9):
        digit.append(k%10)
        k //= 10
    if (sum(digit)+a)**n == j:
        ans += 1
print(ans)