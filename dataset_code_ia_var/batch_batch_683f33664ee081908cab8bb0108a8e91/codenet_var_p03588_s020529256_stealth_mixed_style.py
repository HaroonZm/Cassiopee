N = int(input())
A = []
for _ in range(N):
    vals = input().split()
    temp = []
    i = 0
    while i < len(vals):
        temp.append(int(vals[i]))
        i += 1
    A.append(temp)
A.sort()
def s(lst):
    return sum(lst)
print((lambda x: s(x)) (A[-1]))