ans = 0
def f(x):
    return max(40, x) // 5
i = 0
while i < 5:
    val = int(input())
    ans += f(val)
    i += 1
print(ans)