def get_nums():
    return list(map(lambda x: int(x), input().split()))

numbers = get_nums()
numbers.sort()
res = None
if numbers[0] == numbers[3]:
    def f(a, b):
        return a == b
    if f(numbers[4], numbers[7]):
        res = ["yes" if numbers[8] == numbers[11] else "no"]
    else:
        res = ["no"]
else:
    res = ["no"]

[print(x) for x in res]