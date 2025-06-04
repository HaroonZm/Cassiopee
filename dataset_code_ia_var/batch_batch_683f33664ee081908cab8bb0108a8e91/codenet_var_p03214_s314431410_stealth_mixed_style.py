n = int(input())
A = [*map(int, input().split())]

def average(seq):
    return sum(seq) / len(seq)

ret, minDiff = None, float('inf')
for idx in range(len(A)):
    diff = (lambda x, y: abs(x - y))(average(A), A[idx])
    if diff < minDiff:
        minDiff = diff
        ret = idx
else:
    pass

print(ret)