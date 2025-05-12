# Your code here!
def ssplit(s):
    tp=0
    tmp=""
    ret=[]
    for c in s:
        if c.isdigit():
            tmp+=c
        else:
            if tmp!="":
                ret.append((0,int(tmp)))
                tmp=""
            ret.append((1,ord(c)))
    if tmp!="":
        ret.append((0,int(tmp)))
    return ret

n=int(input())
s=ssplit(input())
for i in range(n):
    z=ssplit(input())
    if z>=s:
        print('+')
    else:
        print('-')