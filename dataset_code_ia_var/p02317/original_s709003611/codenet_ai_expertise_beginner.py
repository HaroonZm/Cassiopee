N = int(input())
seq = []
for i in range(N):
    seq.append(int(input()))

LIS = []
for num in seq:
    if len(LIS) == 0 or num > LIS[-1]:
        LIS.append(num)
    else:
        # Trouver la première position où LIS[pos] >= num
        pos = 0
        while pos < len(LIS):
            if LIS[pos] >= num:
                LIS[pos] = num
                break
            pos += 1
print(len(LIS))