import sys

def get_next_string():
    res=''
    while 1:
        k=sys.stdin.read(1)
        if k.strip()!='':
            res+=k
        elif k!='\r':break
    return res

def main():
    n=int(get_next_string())
    s=get_next_string()
    t=get_next_string()
    ans=n
    i=0
    while i<n:
        trigger=0
        for j in range(n-i):
            if list(s)[i+j]!=t[j]:
                trigger=1
                ans+=1
                break
        if trigger==0: break
        i+=1
    print(ans)

if __name__== '__main__':
    main()