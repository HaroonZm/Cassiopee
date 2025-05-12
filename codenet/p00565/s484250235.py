N = int(input())
line = input().split(" ")
A = [int(line[i]) for i in range(N)]
#print(A)

maxVal = 0
count = 0
for i in range(N):
    if A[i] == 1:
        count+=1
        if maxVal < count:
            maxVal = count
    else:
        count = 0
print(maxVal+1)