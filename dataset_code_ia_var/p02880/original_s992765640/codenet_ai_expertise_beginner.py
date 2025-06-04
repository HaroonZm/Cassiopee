N = int(input())
s = [1,2,3,4,5,6,7,8,9]

found = False
for i in s:
    if N % i == 0:
        if (N // i) in s:
            print("Yes")
            found = True
            break

if not found:
    print("No")