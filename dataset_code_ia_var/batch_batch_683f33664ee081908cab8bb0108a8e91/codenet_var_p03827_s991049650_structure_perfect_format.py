N = int(input())
S = input()
rui = [0]
for s in S:
    if s == 'I':
        var = 1
    else:
        var = -1
    rui.append(rui[-1] + var)
print(max(rui))