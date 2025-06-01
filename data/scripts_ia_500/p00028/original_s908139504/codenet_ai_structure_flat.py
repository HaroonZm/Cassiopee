dic = {}
while True:
    try:
        num = int(raw_input())
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    except EOFError:
        items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        if items:
            max_num = items[0][1]
            for k, v in items:
                if v != max_num:
                    break
                print k
        break