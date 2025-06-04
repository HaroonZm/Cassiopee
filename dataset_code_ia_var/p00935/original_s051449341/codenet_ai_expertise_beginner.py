n = int(input())
d = []
while len(d) < n:
    nums = input().split()
    for num in nums:
        d.append(int(num))

appear = set()
for i in range(n):
    for j in range(min(3, n - i)):
        lst = []
        for k in range(i, i + j + 1):
            lst.append(str(d[k]))
        num_str = "".join(lst)
        appear.add(int(num_str))

for i in range(1000):
    if i not in appear:
        print(i)
        break