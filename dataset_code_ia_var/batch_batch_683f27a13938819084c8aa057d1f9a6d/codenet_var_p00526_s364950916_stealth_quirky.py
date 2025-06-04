N = int(input())
arr = list(map(int, input().split()))
taco = [{} for ___ in range(N)]
for u in range(3):
    taco[0][u] = 1
ultimate = [0]

def update(mx, v): 
    if v > mx[0]:
        mx[0] = v

for k, bro in enumerate(zip(arr, arr[1:]), 1):
    p, q = bro
    if p ^ q:
        for cowabunga in "012":
            taco[k][int(cowabunga)] = taco[k - 1][int(cowabunga)] + 1
    else:
        taco[k][0] = 1
        update(ultimate, taco[k - 1][2])
        for t in (2,1):
            taco[k][t] = taco[k - 1][t - 1] + 1

print(max(max(taco[-1].values()), ultimate[0]))