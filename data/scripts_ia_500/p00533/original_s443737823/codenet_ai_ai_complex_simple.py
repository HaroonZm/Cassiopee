from functools import reduce
h,w=map(int,input().split())
cloud=list(map(lambda _:list(input()),range(h)))
def clever_line(line):
    def clever_acc(acc,elem):
        flag,cnt,res=acc
        if elem=='c':
            return (1,0,res+[0])
        elif flag==0:
            return (flag,cnt,res+[-1])
        else:
            return (flag,cnt+1,res+[cnt+1])
    _,__,res=reduce(clever_acc,line,(0,0,[]))
    return res
for line in cloud:
    print(' '.join(map(str,clever_line(line))) )