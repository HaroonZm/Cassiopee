while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    block = list(map(int, input().split()))

    tmp = 0
    i = 1
    S_flag = False
    while tmp < sum(block):
        tmp = (i * (i + 1)) / 2
        i += 1
    if tmp == sum(block):
        S_flag = True
    else:
        S_flag = False

    if not S_flag:
        print(-1)
    else:
        while True:
            Step_flag = True
            for idx in range(len(block)):
                if block[idx] != idx + 1:
                    Step_flag = False
                    break
            if Step_flag:
                print(count)
                break
            else:
                count += 1
                len_b = len(block)
                for j in range(len_b):
                    block[j] -= 1
                block.append(len_b)
                while 0 in block:
                    block.remove(0)
            if count == 10001:
                print(-1)
                break