ans = 0
def count(use, sum, n, s):
    global ans
    if(sum > s or n < 0):
        return;
    if(n == 0 and s == sum):
        ans += 1
    else:
        for i in range(use + 1, 10):
            count(i, sum + i, n - 1, s)

while(True):
    n = map(int, raw_input().split())
    ans = 0
    if(n[0] == 0 and n[1] == 0):
        break
    count(-1, 0, n[0], n[1])
    print(ans)