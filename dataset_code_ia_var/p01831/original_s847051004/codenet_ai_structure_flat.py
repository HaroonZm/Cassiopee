n = int(input())
s = input()
a = s.find('>')
b = n - s.rfind('<') - 1
if a == -1:
    t = b
elif b == -1:
    t = a
else:
    t = min(a, b)
print(n - t)