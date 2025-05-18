import copy

def main():
    while True:
        n,m,t,p = map(int,input().split())
        if not n and not m and not t and not p:
            return

        dlist,clist = [],[]
        
        for _ in range(t):
            d,c = map(int,input().split())
            dlist.append(d)
            clist.append(c)

        coorlist = [tuple(map(int,input().split())) for _ in range(p)]

        oldm = [[1 for _ in range(m)] for _ in range(n)]

        for d,c in zip(dlist,clist):
            if d == 1: # →
                if 2*c <= n:
                    newm = [[0 for _ in range(m)] for _ in range(n-c)]
                    for i in range(c):
                        for j in range(m):
                            newm[i][j] = oldm[c+i][j] + oldm[c-1-i][j]
                    for i in range(c,n-c):
                        for j in range(m):
                            newm[i][j] = oldm[c+i][j]
                    n = n-c
                else:
                    newm = [[0 for _ in range(m)] for _ in range(c)]
                    for i in range(n-c):
                        for j in range(m):
                            newm[i][j] = oldm[c+i][j] + oldm[c-1-i][j]
                    for i in range(n-c,c):
                        for j in range(m):
                            newm[i][j] = oldm[c-1-i][j]
                    n = c
            else: # ↑
                if 2*c <= m:
                    newm = [[0 for _ in range(m-c)] for _ in range(n)]
                    for i in range(n):
                        for j in range(c):
                            newm[i][j] = oldm[i][c+j] + oldm[i][c-1-j]
                    for i in range(n):
                        for j in range(c,m-c):
                            newm[i][j] = oldm[i][c+j]
                    m = m-c
                else:
                    newm = [[0 for _ in range(c)] for _ in range(n)]
                    for i in range(n):
                        for j in range(m-c):
                            newm[i][j] = oldm[i][c+j] + oldm[i][c-1-j]
                    for i in range(n):
                        for j in range(m-c,c):
                            newm[i][j] = oldm[i][c-1-j]
                    m = c
            oldm = newm

        ans = 0
        for c in coorlist:
            print(oldm[c[0]][c[1]])

def visualize(mmap):
    print("------------------")
    for j in range(len(mmap[0])):
        print('|', end="")
        for i in range(len(mmap)):
            print(mmap[i][len(mmap[0])-1-j], '|', end="")
        print()
    print("------------------")

if __name__ == '__main__':
    main()