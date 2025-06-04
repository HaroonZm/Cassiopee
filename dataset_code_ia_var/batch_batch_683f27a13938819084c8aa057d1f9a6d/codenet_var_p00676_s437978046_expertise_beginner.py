import math

while True:
    try:
        s = raw_input()
        a, l, x = map(int, s.split())
    except EOFError:
        break

    half_a = a / 2.0
    part1 = math.sqrt(l * l - half_a * half_a) * a / 2

    half_l = l / 2.0
    l_plus_x_half = (l + x) / 2.0
    part2 = math.sqrt(l_plus_x_half * l_plus_x_half - half_l * half_l) * half_l * 2

    ANS = part1 + part2

    print ANS