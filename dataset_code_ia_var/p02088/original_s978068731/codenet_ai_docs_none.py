N = int(input())
A = list(map(int, input().split()))
even = 0
odd = 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
if even == 0 or odd == 0:
    print(0)
elif odd % 2 == 1:
    print(N - 1)
else:
    print(N - 2)