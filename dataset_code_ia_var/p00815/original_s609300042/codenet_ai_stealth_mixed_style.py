N=int(input())
i=0
while i<N:
    lst = list()
    while True:
        s = list(map(int, input().split()))
        if s[-1]==0:
            lst += s[:-1]
            break
        lst+=s
    nodes=[]; stack=[]; here=0
    for val in lst:
        if val>0:
            nodes.append([])
            tmp=[here, val-1]
            if stack:
                left=stack[-1]
                left[1]-=1
                nodes[here].append(left[0]);nodes[left[0]].append(here)
                stack.append(tmp)
                while stack and stack[-1][1]==0:
                    stack.pop()
            else:
                stack.append([here,val])
            here+=1
        else:
            u=stack[val-1];u[1]-=1
            v=stack[-1];v[1]-=1
            nodes[u[0]].append(v[0]);nodes[v[0]].append(u[0])
            while stack and stack[-1][1]==0:
                stack.pop()
    enum=enumerate(nodes)
    for j,conn in enum:
        print(str(j+1)+' '+ ' '.join(str(_+1) for _ in sorted(conn)))
    i+=1