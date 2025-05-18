c=0
for _ in range(int(input())):
    _,s,a=input().split()
    a=int(a)
    c+=a if s=='(' else -a
    print(['No','Yes'][not c])