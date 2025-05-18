def p(a):
    print(a)

s=int(input())

list=[s]

while True:
    if list[len(list)-1]%2==0:
        a=list[len(list)-1]/2
    else:
        a=3*list[len(list)-1]+1
    if a in list:
        p(len(list)+1)
        break
    else:
        list.append(a)
        # p(list)