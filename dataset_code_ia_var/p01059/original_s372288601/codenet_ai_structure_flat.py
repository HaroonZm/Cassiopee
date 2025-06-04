n, m = map(int, input().split())
lst = []
i = 0
while i < n:
    lst.append(100000)
    i += 1
a_lst = list(map(int, input().split()))
i = 0
while i < len(a_lst):
    lst[a_lst[i] - 1] = 0
    i += 1
i = 0
while i < n - 1:
    x = lst[i] + 1
    if x < lst[i + 1]:
        lst[i + 1] = x
    i += 1
i = n - 1
while i > 0:
    x = lst[i] + 1
    if x < lst[i - 1]:
        lst[i - 1] = x
    i -= 1
mx = lst[0]
i = 1
while i < n:
    if lst[i] > mx:
        mx = lst[i]
    i += 1
print(mx)