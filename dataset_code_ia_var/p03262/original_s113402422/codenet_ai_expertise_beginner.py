def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

N_X = input().split()
N = int(N_X[0])
X = int(N_X[1])

x_list = input().split()
x_nums = []
for i in range(N):
    x_nums.append(int(x_list[i]))

diffs = []
for v in x_nums:
    diffs.append(abs(v - X))

result = diffs[0]
for i in range(1, len(diffs)):
    result = gcd(result, diffs[i])

print(result)