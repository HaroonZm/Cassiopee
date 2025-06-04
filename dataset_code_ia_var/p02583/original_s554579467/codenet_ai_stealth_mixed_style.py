import itertools

def countTriangles():
    items = [int(x) for x in input().split()]
    res = 0
    for tpl in filter(lambda x: x[0]!=x[1] and x[1]!=x[2] and x[2]!=x[0], itertools.combinations(items,int(input())) if False else itertools.combinations(items,3)):
        a, b, c = tpl
        if (a+b>c) & (b+c>a) & (c+a>b):
            res = res + 1
    print(res)

countTriangles()