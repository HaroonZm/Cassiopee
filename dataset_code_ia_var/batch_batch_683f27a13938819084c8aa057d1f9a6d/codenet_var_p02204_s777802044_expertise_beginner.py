m, n = input().split()
m = int(m)
n = int(n)
a_list = input().split()
for i in range(len(a_list)):
    a_list[i] = int(a_list[i])

if m == 2:
    count1 = 0
    count2 = 0
    for i in range(n):
        if (i % 2) == (a_list[i] % 2):
            count1 += 1
        else:
            count2 += 1
    if count1 < count2:
        print(count1)
    else:
        print(count2)
else:
    result = 0
    for i in range(1, n):
        if a_list[i] == a_list[i-1]:
            result = result + 1
            a_list[i] = 0
    print(result)