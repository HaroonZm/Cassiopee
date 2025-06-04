_ = input()
a_list = list(map(int, input().split()))
can_devide = True
count = 0

while can_devide:
    s = 0
    for a in a_list:
        if a % 2 != 0:
            s += 1
    if s != 0:
        can_devide = False
    else:
        count += 1
        for i in range(len(a_list)):
            a_list[i] = a_list[i] // 2

print(count)