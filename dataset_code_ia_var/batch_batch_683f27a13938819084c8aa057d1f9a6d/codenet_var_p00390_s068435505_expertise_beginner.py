n = int(input())
aw = []
a_input = input().split()
w_input = input().split()

for i in range(n):
    a = int(a_input[i])
    w = int(w_input[i])
    aw.append([a, w])

migimin = 1001
hidarimin = 1001

for i in range(n):
    a = aw[i][0]
    w = aw[i][1]
    if a == 0:
        if w < migimin:
            migimin = w
    else:
        if w < hidarimin:
            hidarimin = w

if hidarimin > 1000 or migimin > 1000:
    print(0)
else:
    print(hidarimin + migimin)