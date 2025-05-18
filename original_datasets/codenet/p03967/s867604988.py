s = input()
l = len(s)
g = s.count('g')
p = s.count('p')
if g >= p:
    print((g - p) // 2)
else:
    print(-(p - g) // 2)