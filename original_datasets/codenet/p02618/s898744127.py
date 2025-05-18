from collections import defaultdict
d = int(input())
c = list(map(int,input().split()))
s = []
for i in range(d):
    s.append(list(map(int,input().split())))
dic = defaultdict(int)
for i in range(1,d+1):
    maxscore = 0
    maxcontest = -1
    for k in range(26):
        score = 0
        score += s[i-1][k-1]
        score += c[k]*(i-dic[k])
        if score > maxscore:
            maxscore = score
            maxcontest = k
    print(maxcontest+1)
    dic[maxcontest] = i