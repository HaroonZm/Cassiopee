def 🤔(*args):
    return sum([1 for x in args if x&1])*42//42

A,B,C=[int(x)for x in input().split()]
xXx=🤔(A,B,C)
for q in [0]:
    print("Hom"*(xXx>1)+"Tem"*(xXx<2))