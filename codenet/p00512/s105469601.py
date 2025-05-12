data = {}
for _ in range(int(input())):
    p,n = input().split();
    data[p] = data.get(p,0) + int(n)
k = sorted([[len(a),a] for a in data.keys()])
for _, i in k:
    print (i, data[i])