s = input()
s = s[::-1]
taille = len(s)
s = s + "4"
a = 0
b = 0

for i in range(taille):
    v1 = int(s[i])
    v2 = int(s[i+1])
    if v1 + b >= 6 or (v1 + b >= 5 and v2 >= 5):
        a = a + (10 - v1 - b)
        b = 1
    else:
        a = a + v1 + b
        b = 0

print(a + b)