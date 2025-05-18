from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break
    
    c = input().split()
    d = defaultdict(int)
    d["hoge"] = 0
    flag = False
    for i in range(n):
        d[c[i]] += 1
        ranking = sorted(d.items(), key=lambda x: x[1], reverse=True)
        if ranking[0][1] > ranking[1][1] + (n - 1 - i):
            print(ranking[0][0] + " " + str(i + 1))
            flag = True
            break
    if not flag:
        print("TIE")