while True:

    n, m = list(map(int, input().split()))

    if n == 0 and m == 0:
        break

    medicines = set(map(int, input().split()))
    weights = list(map(int, input().split()))

    possibles = {0}

    for i in weights:
        pre = possibles.copy()
        for j in possibles:
            plus = i + j
            minus = abs(i - j)
            pre.add(plus)
            pre.add(minus)
        possibles = pre
    possibles.discard(0)

    medicines -= possibles

    if len(medicines) == 0:
        print(0)
        continue

    add = []

    for i in medicines:
        pre_add = {0}
        for j in possibles:
            plus = i + j
            minus = abs(i - j)
            pre_add.add(plus)
            pre_add.add(minus)
            pre_add.add(i)
            pre_add.discard(0)
        add.append(pre_add)

    ans = add[0]

    for i in add:
        pre_ans = ans & i
        ans = pre_ans

    ans_list = []

    for i in ans:
        ans_list.append(i)

    if len(ans_list) == 0:
        print(-1)
    elif len(ans_list) == 1:
        print(ans_list[0])
    else:
        print(min(ans_list))