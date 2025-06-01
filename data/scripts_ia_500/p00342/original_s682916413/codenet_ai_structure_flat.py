n = int(input())
data = list(map(int, input().split()))
data.sort()
data1 = data[:]
A = data1.pop()
B = data1.pop()
min_diff = 10**9
C = D = 0
for i in range(len(data1)-1):
    diff = data1[i+1] - data1[i]
    if diff < min_diff:
        min_diff = diff
        C = data1[i+1]
        D = data1[i]
ans_1 = (A + B) / (C - D)
data2 = data[:]
min_diff = 10**9
for i in range(len(data2)-1):
    diff = data2[i+1] - data2[i]
    if diff < min_diff:
        min_diff = diff
        C = data2[i+1]
        D = data2[i]
data2.remove(C)
data2.remove(D)
A = data2.pop()
B = data2.pop()
ans_2 = (A + B) / (C - D)
print(max(ans_1, ans_2))