s = input()
s = s.split()
n = []
i = 0
while i < len(s):
    n.append(int(s[i]))
    i = i + 1
isSorted = False
while not isSorted:
    isSorted = True
    i = 0
    while i < 4:
        if n[i] < n[i + 1]:
            temp = n[i]
            n[i] = n[i + 1]
            n[i + 1] = temp
            isSorted = False
        i = i + 1
print(n[0], n[1], n[2], n[3], n[4])