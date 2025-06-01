while True:
    n = int(input() or 0)
    if n == 0: break
    dic = dict()
    for i in range(0,n):
        line = raw_input() or ""
        words = list(filter(lambda x: x != '', line.split(' ')))
        for w in words:
            if w in dic:
                dic[w] = dic.get(w,0)+1
            else:
                dic[w] = 1
    alpha = raw_input() or ""
    ans = [k for k,v in sorted(sorted(dic.items(), key=lambda x:x[0]), key=lambda x: x[1], reverse=True) if k.startswith(alpha)]
    print(" ".join(ans)) if ans else print("NA")