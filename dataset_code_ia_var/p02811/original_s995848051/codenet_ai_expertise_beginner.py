k_x = input().split()
K = int(k_x[0])
X = int(k_x[1])

if 500 * K >= X:
    print("Yes")
else:
    print("No")