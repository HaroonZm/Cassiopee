a = input()
b = input()
reversed_b = ""
for i in range(len(b) - 1, -1, -1):
    reversed_b = reversed_b + b[i]
if a == reversed_b:
    print("YES")
else:
    print("NO")