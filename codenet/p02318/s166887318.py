s1 = raw_input()
s2 = raw_input()

a = [[0 for i in range(len(s2) + 1)]for i in range(len(s1) + 1)]
for i in range(len(s2) + 1):
    a[0][i] = i
for i in range(len(s1) + 1):
    a[i][0] = i
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            a[i+1][j+1] = a[i][j]
        else:
            a[i+1][j+1] = min([a[i][j+1], a[i+1][j], a[i][j]]) + 1
print a[len(s1)][len(s2)]