N = int(input())
line = input().split(" ")
A = []
for i in range(N):
    A.append(int(line[i]))
maxVal = 0
count = 0
for i in range(N):
    if A[i] == 1:
        count = count + 1
        if maxVal < count:
            maxVal = count
    else:
        count = 0
print(maxVal + 1)