from itertools import product

N,M = map(int,input().split())

ABC = [list(map(int,input().split())) for i in range(N)]
ans = 0
for a,b,c in product([-1,1],repeat=3):
    score = []
    for x,y,z in ABC:
        score.append(x * a + y * b + z * c)
    score.sort(reverse=True)
    ans = max(ans,sum(score[:M]))

print(ans)