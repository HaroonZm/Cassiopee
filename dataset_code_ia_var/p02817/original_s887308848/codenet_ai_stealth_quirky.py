def o():return input()
def splitz(x):return x.split()
def mappy(f,x):return list(map(f,x))
st = o()
x, y = mappy(str, splitz(st))
arr = [y, x]
print(''.join(arr))