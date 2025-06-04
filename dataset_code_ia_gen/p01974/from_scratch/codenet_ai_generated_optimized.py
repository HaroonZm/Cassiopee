N=int(input())
a=list(map(int,input().split()))
mod_dict={}
for x in a:
    r=x%(N-1)
    if r in mod_dict:
        print(mod_dict[r], x)
        break
    mod_dict[r]=x