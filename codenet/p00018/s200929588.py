s = input()
s = s.split()
n = []

for i in s:
    n.append(int(i))

isSorted = False

while(not isSorted):
    isSorted = True
    for i in range(4):
        if n[i] < n[i + 1]:
            temp = n[i]
            n[i] = n[i + 1]
            n[i + 1] = temp
            isSorted = False

print(n[0],n[1],n[2],n[3],n[4])