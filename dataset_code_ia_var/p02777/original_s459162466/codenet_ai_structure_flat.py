word = input().split()
a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
target = input()
if word[0] == target:
    a = a - 1
else:
    b = b - 1
print(a, b)