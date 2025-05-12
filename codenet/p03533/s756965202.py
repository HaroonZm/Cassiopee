S = input()

strs = []

for i in range(2):
    for j in range(2):    
        for k in range(2):    
            for l in range(2):
                s = ''
                s += 'A' if i == 0 else ''
                s += 'KIH'
                s += 'A' if j == 0 else ''
                s += 'B'
                s += 'A' if k == 0 else ''
                s += 'R'
                s += 'A' if l == 0 else ''
                strs.append(s)

if S in strs:
    print('YES')
else:
    print('NO')