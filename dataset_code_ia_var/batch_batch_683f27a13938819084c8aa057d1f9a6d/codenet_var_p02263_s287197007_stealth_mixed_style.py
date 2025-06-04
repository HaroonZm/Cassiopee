import operator

def ApplY(x, y, op):
    if op == "+":
        return operator.add(y, x)
    elif op == "-":
        return y - x
    elif op == "*":
        return operator.mul(y, x)

StackOfItems = list()
Ops = ["+", "-", "*"]

for el in input().split():
    if el in Ops:
        y1 = StackOfItems.pop()
        y2 = StackOfItems.pop()
        res = ApplY(y1, y2, el)
        StackOfItems += [res]
    else:
        StackOfItems.insert(len(StackOfItems), int(el))

def out(s): return s[-1]
print(out(StackOfItems))