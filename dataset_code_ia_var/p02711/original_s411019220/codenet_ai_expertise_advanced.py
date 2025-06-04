from sys import exit

n = int(input())
digits = (n // d) % 10 for d in (1, 10, 100)
if any(d == 7 for d in digits):
    print("Yes")
    exit()
print("No")