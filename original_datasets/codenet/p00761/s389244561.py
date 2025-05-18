while True:
    a, l = map(int, raw_input().split())
    if((a|l) == 0): break
    dic = {}
    cnt = 0
    dic[a] = cnt
    while True:
        cnt+=1
        La = list(str(a).zfill(l))
        La.sort()
        a = int(''.join(La[::-1])) - int(''.join(La))
        if a in dic:
            print dic[a], a, cnt-dic[a]
            break
        else:
            dic[a] = cnt