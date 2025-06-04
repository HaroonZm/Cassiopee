l, c = map(int, input().split())
tbl = []
li_sum = [0 for _ in range(c+1)]
i = 0
while i < l:
    tblS = input()
    row = list(map(int, tblS.split()))
    tbl.append(row)
    print(tblS, end='')
    s = 0
    j = 0
    while j < c:
        s += row[j]
        li_sum[j] += row[j]
        j += 1
    print(' ', s, sep='')
    li_sum[c] += s
    i += 1
print(' '.join(str(x) for x in li_sum))