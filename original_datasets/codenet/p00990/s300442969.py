import itertools

n = int(input())
id = input()[::-1]
count = 0
a = []
odd, even = 0 , 0
tmp = 0
for i in range(1,n+1):
    if id[i-1] == "*":
        if i % 2:
            odd += 1
        else:
            even += 1
    elif i % 2 == 0:
        x = int(id[i-1])
        if x >= 5:
            tmp += (x * 2 - 9)
        else:
            tmp += (x * 2)
    else:
        tmp += (int(id[i-1]))
m = int(input())

data = list(map(int, input().split()))

def sum2(ls):
    ans = 0
    for k in ls:
        if k >= 5:
            ans += (k * 2 - 9)
        else:
            ans += (k * 2)
    return ans

odd_list = list(map(lambda x: (sum(x) % 10),list(itertools.product(data, repeat=odd))))
even_list = list(map(lambda x: ((sum2(x)) % 10),list(itertools.product(data, repeat=even))))
odd_mod = [odd_list.count(i) for i in range(10)]
even_mod = [even_list.count(i) for i in range(10)]
for i in range(10):
    for j in range(10):
        if ((i + j + tmp) % 10) == 0:
            count += odd_mod[i] * even_mod[j]

print(count)