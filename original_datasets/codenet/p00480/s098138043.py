N=int(input())
number=[int(i) for i in input().split(" ")]
a=number.pop(-1)

if number[0]==0:
    N-=1
    number.pop(0)

numbermap=[[0 for i in range(21)] for j in range(N)]

numbermap[0][0]=1

for i in range(N-1):
    for j in range(21):
        if j+number[i]<=20:
            numbermap[i+1][j+number[i]]+=numbermap[i][j]
        if j-number[i]>=0:
            numbermap[i+1][j-number[i]]+=numbermap[i][j]

print (numbermap[-1][a])