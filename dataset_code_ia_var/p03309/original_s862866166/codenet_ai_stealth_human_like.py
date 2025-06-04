import statistics as stats

# ok, getting N, standard stuff
N=int(input())
A = list(map(int, input().split()))
# adjust with index? not sure why but probably needed for something
for i in range(len(A)):
    A[i]=A[i]-i

med = int(stats.median(A)) # get median, floor I guess

results = []
for val in range(med-2, med+3):
    acc = 0
    for x in A:
        acc += abs(x-val)
    results.append(acc)

# Just take the smallest, easy
print(min(results))