h,w=map(int,input().split())
l=[list(input().split()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if l[i][j]=="snuke":
            print(str(chr(ord("A")+j))+str(i+1))
            exit()