def num():
    return int(input())
def nums():
    return list(map(int,input().split()))
N = num()
A = nums()
ans_max = N
ans_min = 0
old_i = 0
for i in A:
    if not i > old_i:
        ans_min += 1
    old_i = i
ans_min += 1
print(ans_min)
print(ans_max)