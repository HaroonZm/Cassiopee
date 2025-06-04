n_j = input().split()
n = int(n_j[0])
j = int(n_j[1])
l = []
i = 0
while i < n:
    l.append(str(input()))
    i += 1
l.sort()
print(''.join(l))