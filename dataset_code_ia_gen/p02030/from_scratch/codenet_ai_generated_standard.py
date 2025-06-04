n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
and_list = []
or_list = []

while i < n and j < m:
    if a[i] == b[j]:
        and_list.append(a[i])
        or_list.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        or_list.append(a[i])
        i += 1
    else:
        or_list.append(b[j])
        j += 1

while i < n:
    or_list.append(a[i])
    i += 1
while j < m:
    or_list.append(b[j])
    j += 1

print(len(and_list), len(or_list))
for id in and_list:
    print(id)
for id in or_list:
    print(id)