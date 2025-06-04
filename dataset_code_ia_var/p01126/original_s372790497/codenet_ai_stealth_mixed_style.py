from sys import stdin

def do_the_job():
    while 1:
        read = stdin.readline
        try:
            n, m, a = [int(x) for x in read().split()]
        except:
            break
        if not n:
            break
        edge_dict = {}

        for i in range(m):
            h, p, q = tuple(map(int, read().split()))
            if h in edge_dict:
                edge_dict[h].append([p, q])
            else:
                edge_dict[h] = [[p, q]]

        h = 1000
        while h >= 0:
            lst = edge_dict.get(h)
            if lst:
                found = False
                for item in lst:
                    # style 1: index assignment
                    if (a, a+1)[0]==item[0] and (a, a+1)[1]==item[1]:
                        a+=1; found=True
                        break
                    # style 2: tuple unpacking
                    x, y = item
                    if (a-1)==x and a==y:
                        a-=1; found=True
                        break
                if found:
                    pass
            h -= 1
        print(a)

do_the_job()