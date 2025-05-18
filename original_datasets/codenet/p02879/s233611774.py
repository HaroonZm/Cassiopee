ab = input()
a, b = ab.split(" ")
A = int(a)
B = int(b)

if "0" in a or "0" in b or A > 9 or B > 9:
    print(-1)
else:
    print(A * B)