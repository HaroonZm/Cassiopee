dic = {}
while True:
    try:
        num = int(raw_input())
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] = dic[num] + 1
    except EOFError:
        max_num = 0
        index = 0
        for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
            if index == 0:
                max_num = v
            if max_num != v:
                break
            print k
            index += 1
        break