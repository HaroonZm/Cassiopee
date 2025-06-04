x, y, z = (int(e) for e in input().split())
def get_costs(a, b, c):
    return [abs(a-b), abs(b-c), abs(c-a)]
class Result:
    pass
Result.value = 0
for idx, val in enumerate(sorted(get_costs(x, y, z))):
    if idx < 2:
        Result.value += val
else:
    print(Result.value)