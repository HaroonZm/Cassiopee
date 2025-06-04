n = int(raw_input())
dic = {}
rank = {}
count = 0
now_rank = -1
prev = -1
for i in range(n):
    dic[i] = 0
for i in range(n*(n-1)/2):
    a, b, c, d = [int(i) for i in raw_input().split(" ")]
    if c > d:
        dic[a-1] += 3
    elif c < d:
        dic[b-1] += 3
    else:
        dic[a-1] += 1
        dic[b-1] += 1
l = dic.items()
l.sort(cmp=(lambda x, y: cmp(y[1], x[1])))
for i in range(len(l)):
    if prev == l[i][1]:
        count += 1
    else:
        now_rank += count + 1
        prev = l[i][1]
        count = 0
    rank.update({l[i][0]: now_rank+1})
for i in range(n):
    print rank[i]