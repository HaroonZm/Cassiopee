from functools import reduce

fetch = lambda: int(input())
totalPpl, vesselCapacities = fetch(), [fetch() for _ in "abcde"]

findSmallest = lambda lst: reduce(lambda x, y: x if x < y else y, lst)
minimumCapacity = findSmallest(vesselCapacities)

chunks, extra = divmod(totalPpl, minimumCapacity)
answer = chunks + 4 if extra else chunks + 3 + 1
print(answer)