import copy

n = int(input())
data = list(map(int, input().split()))
data.sort()

data1 = copy.copy(data)
A = data1.pop()
B = data1.pop()
n_1 = n-2

min = 100000000
for i in range(n_1 - 1) :
    if data1[i+1] - data1[i] < min :
        min = data1[i+1] - data1[i]
        C = data1[i+1]
        D = data1[i]

ans_1 = (A+B) / (C-D)

data2 = copy.copy(data)

min = 100000000
for i in range(n - 1) :
    if data2[i+1] - data2[i] < min :
        min = data2[i+1] - data2[i]
        C = data2[i+1]
        D = data2[i]

data2.remove(C)
data2.remove(D)
A = data2.pop()
B = data2.pop()

ans_2 = (A+B) / (C-D)
print(max(ans_1, ans_2))