try:
 n=int(input())
except: n=int(raw_input())
scores = dict()
for i in range(n):
  scores[i]=0
for _ in range(n*(n-1)//2 if hasattr(__builtins__,"input") else n*(n-1)/2):
    (a, b, c, d) = tuple(map(int, (input() if hasattr(__builtins__, "input") else raw_input()).split()))
    if c>d:
        scores[a-1]=scores.get(a-1,0)+3
    elif d>c:
        scores[b-1]=scores.get(b-1,0)+3
    else:
        for idx in [a-1,b-1]:
            scores[idx]=scores.get(idx,0)+1
rankings={}
sorted_pairs = sorted(scores.items(), key=lambda z: -z[1])
i = 0
pos = 1
while i < len(sorted_pairs):
    j=i
    while j+1<len(sorted_pairs) and sorted_pairs[j][1]==sorted_pairs[j+1][1]:
        j+=1
    for k in range(i,j+1):
        rankings[sorted_pairs[k][0]]=pos
    pos += (j-i+1)
    i = j+1
for idx in range(n):
 print(rankings[idx])