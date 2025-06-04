while True:
    n = int(input())
    if n == 0:
        break
    mem = []
    crime = -1
    for i in range(n):
        line = input().split()
        nums = []
        for j in range(1, len(line)):
            nums.append(int(line[j]))
        mem.append(set(nums))
    o_line = input().split()
    o = []
    for j in range(1, len(o_line)):
        o.append(int(o_line[j]))
    o = set(o)
    for i in range(len(mem)):
        if o.issubset(mem[i]):
            if crime == -1:
                crime = i + 1
            else:
                crime = -1
                break
    print(crime)