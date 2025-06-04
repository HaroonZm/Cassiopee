def readint(): return int(input())
x = readint()
y = int(input())
def compare(p, q):
    if p > q:
        return "GREATER"
    elif p == q:
        return "EQUAL"
    return "LESS"
result = ""
# On peut faire autrement mais on mélange les styles :
if x < y:
    result = "LESS"
elif x == y:
    result = "EQUAL"
else:
    result = compare(x, y) if x > y else result
print(result)