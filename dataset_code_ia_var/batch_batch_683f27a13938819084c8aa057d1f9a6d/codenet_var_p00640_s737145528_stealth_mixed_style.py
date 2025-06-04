import sys

if __name__ == '__main__':

    def do_input():
        return sys.stdin.readline().strip()

    n = int(do_input())
    while n != 0:
        _ = do_input()
        pagelist = []
        namedict = dict()
        idx = 0
        for _ in range(n):
            tmp = do_input().split()
            pagename = tmp[0]
            btnnum = int(tmp[1])
            namedict[pagename] = idx
            index = 0
            l = []
            while index < btnnum:
                line = do_input().split()
                l.append((int(line[0]),int(line[1]),int(line[2]),int(line[3]),line[4]))
                index += 1
            pagelist.append((pagename,l))
            idx += 1

        buf=[None]*2000
        buf[0]=0
        now=0
        length=1

        m = int(do_input())
        cnt=0
        while cnt<m:
            arr = do_input().split()
            if arr[0] == "back":
                now = now-1 if now > 0 else now
            elif arr[0] == "forward":
                now = now+1 if now < length-1 else now
            elif arr[0] == "show":
                def show():
                    print(pagelist[buf[now]][0])
                show()
            else:
                def click(buf,now,length):
                    px,py = map(int,(arr[1],arr[2]))
                    for bt in pagelist[buf[now]][1]:
                        if all([bt[0]<=px<=bt[2],bt[1]<=py<=bt[3]]):
                            now+=1
                            buf[now]=namedict[bt[4]]
                            length=now+1
                            break
                    return now,length
                now,length = click(buf,now,length)
            cnt+=1

        n = int(do_input())