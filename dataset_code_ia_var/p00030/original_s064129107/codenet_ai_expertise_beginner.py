ans = 0

def count(use, sum_val, n, s):
    global ans
    if sum_val > s or n < 0:
        return
    if n == 0 and sum_val == s:
        ans += 1
        return
    for i in range(use + 1, 10):
        count(i, sum_val + i, n - 1, s)

while True:
    user_input = raw_input().split()
    n = int(user_input[0])
    s = int(user_input[1])
    ans = 0
    if n == 0 and s == 0:
        break
    count(-1, 0, n, s)
    print(ans)