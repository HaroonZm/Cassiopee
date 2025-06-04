getNumber = lambda : int(input())
getList = lambda : [*map(int, input().split())]
length = getNumber()
stuff = getList()
val = [0]
for idx in range(length-2):
    sliceMe = stuff[idx:idx+3]
    middle = sliceMe[1]
    if min(sliceMe) < middle < max(sliceMe):
        val[0] += 1
print(val.pop())