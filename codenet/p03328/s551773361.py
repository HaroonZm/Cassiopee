a, b = map(int, input().split())

diff = b - a
for n in range(1000):
    if diff == n + 1:
        ans = n * (n + 1) // 2 - a
        print(ans)

# a = n * (n + 1) // 2
# b = (n * 1) * (n + 2) // 2

# b - a = (n**2 + 3 * n + 2 - N** 2 - n) // 2
# b - a = (2 * n + 2) // 2
# b - a = n + 1