n,m=[int(s)for s in input().split(" ")]
bibs=[int(input())for i in range(n)]
for k in range(1,m+1):
    for i in range(n-1):
        if bibs[i]%k>bibs[i+1]%k:(bibs[i],bibs[i+1])=(bibs[i+1],bibs[i])
for bib in bibs:print(bib)