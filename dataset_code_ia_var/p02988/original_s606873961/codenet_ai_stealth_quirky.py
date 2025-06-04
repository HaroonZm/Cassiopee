from collections import deque

N = int(input())
P = list(map(int, input().split()))
Counter = 0

Buffer = deque(maxlen=3)
for idx, value in enumerate(P):
    Buffer.append(value)
    if len(Buffer)==3:
        sample = Buffer.copy()
        sample.sort()
        if Buffer[1] == sample[1]:
            Counter += 1

print(+Counter)