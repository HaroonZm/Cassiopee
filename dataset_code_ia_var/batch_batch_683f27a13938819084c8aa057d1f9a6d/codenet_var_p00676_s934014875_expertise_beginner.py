import math

def surface(a, b):
    s = b + a / 2.0
    return math.sqrt(s * (s - a) * ((s - b) ** 2))

while True:
    try:
        inputs = raw_input()
        a, l, x = map(int, inputs.split())
        part1 = surface(a, l)
        part2 = surface(l, (l + x) / 2.0)
        print part1 + 2 * part2
    except:
        break