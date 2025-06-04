dic = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}

while True:
    sa = input().split()
    a = int(sa[0])
    b = int(sa[1])
    if a == 0 and b == 0:
        break

    lst = []
    lst.append(a + b)
    for i in range(4):
        nums = input().split()
        x = int(nums[0])
        y = int(nums[1])
        lst.append(x + y)

    max_val = lst[0]
    max_index = 0
    for i in range(1, 5):
        if lst[i] > max_val:
            max_val = lst[i]
            max_index = i

    print(dic[max_index], max_val)