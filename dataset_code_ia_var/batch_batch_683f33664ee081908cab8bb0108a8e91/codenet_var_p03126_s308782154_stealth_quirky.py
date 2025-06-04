from collections import Counter as Cnt

def get_input():
    return input()

N_M_tuple = tuple(int(e) for e in get_input().split())
counter_stuff = []
[N, M] = list(N_M_tuple)

add = counter_stuff.extend
for _ in range(N):
    line = list(map(int, get_input().split()))
    ingredients = {val for val in line[1:]}
    [add([ingredient]) for ingredient in ingredients]

cnt = Cnt(counter_stuff)
result = sum([1 for k, v in cnt.items() if v==N])
print(result)