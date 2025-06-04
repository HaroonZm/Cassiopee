n = list(map(int, input()))
cnt = 1
for i in range(1, 4):
    if n[i] == n[i-1]:
        cnt += 1
        if cnt == 3:
            print("Yes")
            break
    else:
        cnt = 1
else:
    print("No")