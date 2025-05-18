import queue
while 1:
    n=int(input())
    if n==0:
        break
    dic={}
    for i in range(n):
        k,s=input().split()
        dic[k]=s
    s=input()
    ans=input()
    q=queue.Queue()
    q.put((s,0))
    find=False
    while not q.empty():
        s=q.get()
        if s[0]==ans:
            print(s[1])
            q=queue.Queue()
            find=True
        if not find:
            for k in dic.keys():
                t=s[0].replace(k,dic[k])
                if len(t)<=len(ans) and s[0]!=t:
                    q.put((t,s[1]+1))
    if not find:
        print(-1)