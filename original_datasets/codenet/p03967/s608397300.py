# https://atcoder.jp/contests/arc062/tasks/arc062_b

S = input()
N = len(S)

num = 0
ans = 0
for i in range(N):
    if S[i] == 'g':
        if num > 0:
            num -= 1
            ans += 1
        else:
            num += 1
    else:
        if num > 0:
            num -= 1
        else:
            num += 1
            ans -= 1

# print(S, num, ans)
print(ans)