N,A,B = map(int, input().split())

lst = []
for _ in range(N):
    val = int(input())
    lst.append(val)

def counter(seq):
    res = 0
    idx = 0
    while idx < len(seq):
        if seq[idx] < A or seq[idx] >= B:
            res = res + 1
        idx += 1
    return res

print(counter(lst))