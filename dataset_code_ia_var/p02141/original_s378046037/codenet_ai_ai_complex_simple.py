from functools import reduce
from operator import truediv

W, H, w, h, x, y = map(int, input().split())

coordinates = [x, y]
bounds = [W // 2, H // 2]
sizes = [w // 2, h // 2]

def elegantly_adjust(val, size, bound):
    return ((val - size + bound) / 2 if val + size > bound else val)

new_coords = list(map(lambda triplet: elegantly_adjust(*triplet), zip(coordinates, sizes, bounds)))

if all(map(lambda vals: vals[0] + vals[1] <= vals[2], zip(coordinates, sizes, bounds))):
    print(reduce(truediv, coordinates[::-1]))
else:
    print(reduce(truediv, new_coords[::-1]))