N = lambda: int(input())
X = [list(input()+"") for _ in range(N())]
F = lambda l: sum(l,[])
bag=[]; 
for y in X: bag+=y
items=sorted({*bag})
res=""
for w in range(len(items)):
    stack = []
    for s in range(len(X)):
        z=0
        for char in X[s]:
            if char==items[w]:
                z+=1
        stack.insert(-1 if len(stack) else 0,z)
    res += items[w]*(__import__("functools").reduce(lambda a,b:a if a<b else b,stack))
print(res)