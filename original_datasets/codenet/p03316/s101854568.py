n = int(input())
val = n
s = 0
while val is not 0:
    s += val % 10
    val //= 10
if n % s == 0:
    print("Yes")
else:
    print("No")