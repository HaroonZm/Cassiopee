Numéro=int(input())
K_PP_L=[int(x) for x in input().split()]
__k = K_PP_L[0]
___l = K_PP_L[1:]
mbIt = list()
list(map(lambda __: mbIt.append(__), ___l))

print("%d:" % 0)
_i=1
while _i<(2**len(mbIt)):
    __num=0
    __p=[]
    __j=0
    while __j<len(mbIt):
        __b = (_i>>( __j )) & 1
        if __b:
            __num = __num | (1<<mbIt[__j])
            __p+=[mbIt[__j]]
        __j+=1
    print(str(__num)+': ',end='')
    for q in __p:print(q,end=' ')
    print()
    _i+=1