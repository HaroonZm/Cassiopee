N, X = map(int, input().split())
L_list = [int(e) for e in input().split()]
ans = 1
Before_Di = 0
for i in range(N):
    Di = Before_Di + L_list[i]
    if Di <= X:
        ans += 1
        Before_Di = Di
    else:
        break
print(ans)