N = list(input())
ans = "No"
before_num = N[0]

tmp = 1
for i in range(1, len(N)):
    if N[i] == before_num:
        tmp += 1
        if tmp == 3:
            ans = "Yes"
            break
    else:
        tmp = 1
        before_num = N[i]

print(ans)