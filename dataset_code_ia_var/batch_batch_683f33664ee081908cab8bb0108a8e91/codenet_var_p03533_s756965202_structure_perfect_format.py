S = input()

strs = []

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                s = ''
                if i == 0:
                    s += 'A'
                s += 'KIH'
                if j == 0:
                    s += 'A'
                s += 'B'
                if k == 0:
                    s += 'A'
                s += 'R'
                if l == 0:
                    s += 'A'
                strs.append(s)

if S in strs:
    print('YES')
else:
    print('NO')