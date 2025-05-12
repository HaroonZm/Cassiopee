a = input()
setA = set(map(int, input().split()))
b = input()
setB = set(map(int, input().split()))

for elem in sorted(setA.difference(setB)):
    print(elem)