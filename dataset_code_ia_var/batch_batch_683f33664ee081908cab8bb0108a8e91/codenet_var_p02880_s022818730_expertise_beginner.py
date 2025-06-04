n = int(input())
found = False

for i in range(1, 10):
    if n % i == 0:
        if n // i <= 9:
            found = True
            break

if found:
    print("Yes")
else:
    print("No")