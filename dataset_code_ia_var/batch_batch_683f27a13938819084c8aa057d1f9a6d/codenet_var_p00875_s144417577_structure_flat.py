import queue
while True:
    n = int(input())
    if n == 0:
        break
    dic = {}
    i = 0
    while i < n:
        k, v = input().split()
        dic[k] = v
        i += 1
    s = input()
    ans = input()
    q = queue.Queue()
    q.put((s, 0))
    find = False
    while not q.empty():
        elem = q.get()
        if elem[0] == ans:
            print(elem[1])
            q = queue.Queue()
            find = True
        if not find:
            for k in dic:
                t = elem[0].replace(k, dic[k])
                if len(t) <= len(ans) and elem[0] != t:
                    q.put((t, elem[1]+1))
    if not find:
        print(-1)