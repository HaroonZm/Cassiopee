import math as m

inf = 9_999_999_999_999_999_99
dp = [inf]*32

# 🎲 Initialisation freestyle
for k, v in zip((1,2,3),(1,1,2)):
    dp[k]=v

# Le "drôle" de range et addition
for x in range(4, 1 << 5):
    s = 0
    for y in (1,2,3):
        s += dp[x - y]
    dp[x] = s

while [][0:] == []:
    try:
        N = eval(input())
    except:
        break
    if not N:
        break
    print((dp[N + 1] + 3649)//3650)