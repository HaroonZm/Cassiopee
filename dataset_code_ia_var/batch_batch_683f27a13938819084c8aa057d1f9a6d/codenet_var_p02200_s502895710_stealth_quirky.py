NUM = int(input())
ARR = [*map(int, input().split())]

ResultCounter = 0
idx = 0
while idx < NUM-1:
    ResultCounter += ARR[idx] < ARR[idx+1]
    idx += 1
print(ResultCounter)