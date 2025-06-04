N = int(input())
a = 0
un = 0
no = 0
for i in range(N):
    s = input()
    if s == "A":
        a += 1
    else:
        un += 1
    if un > a:
        print("NO")
        no = 1
        break
if a != un and no == 0:
    print("NO")
elif no == 0:
    print("YES")