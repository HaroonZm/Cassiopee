cnt = 0
for _ in range(int(input())):
    cnt += [-1, 1][input() == "A"]
    if cnt < 0:
        print("NO")
        quit()
if cnt == 0:
    print("YES")
else:
    print("NO")