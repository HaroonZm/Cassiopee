def minDist(vals):
    res = [abs(vals[0]-vals[1]), abs(vals[0]-vals[2])]
    if res[0] < res[1]:
        return 'A'
    else:
        return 'B'

inputs = input().split()
x = int(inputs[0])
a = int(inputs[1])
b = int(inputs[2])

print((lambda r: r)(minDist([x,a,b])))