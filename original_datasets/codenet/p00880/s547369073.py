from functools import reduce
import math

def length(p1, p2):
    sub2 = [(a - b)**2 for a, b in zip(p1, p2)]
    return math.sqrt(sum(sub2))

def r_center(lines):
    lines_sum = reduce(lambda a, b: a + b, lines)
    s = lines_sum / 2
    area = math.sqrt(s * (s - lines[0]) * (s - lines[1]) * (s - lines[2]))
    return 2 * area / (lines_sum)

def r_length(lines, r_center):
    x = (lines[0] + lines[2] - lines[1]) / 2
    b_l = math.sqrt(x**2 + r_center**2)
    a_l = math.sqrt((lines[2] - x)**2 + r_center**2)
    c_l = math.sqrt((lines[0] - x)**2 + r_center**2)
    return [a_l, b_l, c_l]

while True:
    positions = list(map(int, input().split()))
    if reduce(lambda a, b: a | b, positions) == 0:
        break
    p1, p2, p3 = [[i, j] for i, j in zip(positions[::2], positions[1::2])]

    lines = [length(a, b) for a, b in ((p1, p2), (p2, p3), (p3, p1))]
    lines_sum = reduce(lambda a, b: a + b, lines)

    r_c = r_center(lines)
    round_half = lines_sum / 2
    rc_len = r_length(lines, r_c)

    r1 = r_c * (round_half + rc_len[0] - r_c - rc_len[1] -
                rc_len[2]) / (2 * (round_half - lines[0]))
    r2 = r_c * (round_half + rc_len[1] - r_c - rc_len[0] -
                rc_len[2]) / (2 * (round_half - lines[1]))
    r3 = r_c * (round_half + rc_len[2] - r_c - rc_len[1] -
                rc_len[0]) / (2 * (round_half - lines[2]))

    print(r2, r3, r1)