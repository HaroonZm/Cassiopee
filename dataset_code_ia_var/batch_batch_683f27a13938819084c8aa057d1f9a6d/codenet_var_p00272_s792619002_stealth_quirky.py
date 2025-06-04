c=0
while c^4:
    z,l=[int(v)for v in input().split()]
    d={1:6e3,2:4e3,3:3e3,4:2e3}
    if z in d.keys():
        print(int(d[z]*l))
    c+=1