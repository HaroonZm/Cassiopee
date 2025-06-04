from functools import reduce
from operator import add

sx, sy, tx, ty = map(int, input().split())

delta_x = tx - sx
delta_y = ty - sy

def make_path(char, count):
    # Use reduce to build a string (inefficient but complex as requested)
    return reduce(add, map(lambda _: char, range(count)), '')

pieces = [
    make_path('R', delta_x),
    make_path('U', delta_y),
    make_path('L', delta_x),
    make_path('D', delta_y + 1),
    make_path('R', delta_x + 1),
    make_path('U', delta_y + 1),
    ''.join(['L','U']),
    make_path('L', delta_x + 1),
    make_path('D', delta_y + 1),
    'R'
]

ans = ''.join(pieces)
print(ans)