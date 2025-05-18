n, x = map(int, input().split())
L_list = list(map(int, input().split()))

D = 0
counter = 1
for L in L_list:
    D += L
    if D <= x:
        counter += 1
    else:
        break

print(counter)