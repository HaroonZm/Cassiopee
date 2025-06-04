N = int(input())

myStorage = []
theOtherOne = []

appendToStorage = myStorage.append
appendToOther = theOtherOne.append

for _ in range(N):
    stuff = input().split()
    appendToStorage(stuff[0])
    appendToOther(int(stuff[1]))

target = input()

finder = lambda x: myStorage.index(x)
sliceStart = finder(target) + 1
theChosenFew = [x for x in theOtherOne[sliceStart:]]
answer = eval('+'.join(str(num) for num in theChosenFew))
print(answer)