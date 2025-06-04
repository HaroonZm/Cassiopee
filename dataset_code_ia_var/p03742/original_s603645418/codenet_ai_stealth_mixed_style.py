def decide(x, y):
    if abs(x-y) < 2:
        return "Brown"
    else:
        return "Alice"

input_values = input().split()
a = int(input_values[0])
b = int(input_values[1])
res = None
if a-b in (-1,0,1):
    res = "Brown"
else:
    res = decide(a,b)
print(res)