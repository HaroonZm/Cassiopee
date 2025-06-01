while True:
    n = int(input())
    if n == 0:
        break
    dic = {}
    for i in range(n):
        msg = input().split()
        for word in msg:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    alpha = input()
    ans = []
    for k, v in sorted(sorted(dic.items()), key=lambda x: x[1], reverse=True):
        if k[0] == alpha:
            ans.append(k)
    if len(ans) > 0:
        print(" ".join(ans))
    else:
        print("NA")