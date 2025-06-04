paper = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    paper.append(row)

while True:
    try:
        s = input()
    except:
        break
    if not s:
        break
    try:
        xys = s.split(',')
        x = int(xys[0])
        y = int(xys[1])
        s_val = int(xys[2])
    except:
        break
    if s_val == 1:
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if abs(x - i) + abs(y - j) <= 1:
                    paper[i][j] = paper[i][j] + 1
                j += 1
            i += 1
    elif s_val == 2:
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if abs(x - i) <= 1 and abs(y - j) <= 1:
                    paper[i][j] = paper[i][j] + 1
                j += 1
            i += 1
    else:
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if abs(x - i) + abs(y - j) <= 2:
                    paper[i][j] = paper[i][j] + 1
                j += 1
            i += 1

ls = []
i = 0
while i < 10:
    j = 0
    while j < 10:
        ls.append(paper[i][j])
        j += 1
    i += 1
cnt = 0
mx = 0
k = 0
while k < len(ls):
    if ls[k] == 0:
        cnt += 1
    if ls[k] > mx:
        mx = ls[k]
    k += 1
print(cnt)
print(mx)