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
if a != un and not no:
    print("NO")
elif not no:
    print("YES")