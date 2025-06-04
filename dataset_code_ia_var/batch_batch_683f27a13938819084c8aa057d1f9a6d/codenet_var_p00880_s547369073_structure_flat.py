from functools import reduce
import math

while True:
    positions = list(map(int, input().split()))
    if reduce(lambda a, b: a | b, positions) == 0:
        break
    p1 = [positions[0], positions[1]]
    p2 = [positions[2], positions[3]]
    p3 = [positions[4], positions[5]]
    a1 = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    a2 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
    a3 = (p3[0] - p1[0])**2 + (p3[1] - p1[1])**2
    l1 = math.sqrt(a1)
    l2 = math.sqrt(a2)
    l3 = math.sqrt(a3)
    lines = [l1, l2, l3]
    lines_sum = l1 + l2 + l3
    s = lines_sum / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    r_c = 2 * area / lines_sum
    round_half = lines_sum / 2
    x = (l1 + l3 - l2) / 2
    b_l = math.sqrt(x * x + r_c * r_c)
    a_l = math.sqrt((l3 - x)**2 + r_c * r_c)
    c_l = math.sqrt((l1 - x)**2 + r_c * r_c)
    rc_len = [a_l, b_l, c_l]
    r1 = r_c * (round_half + rc_len[0] - r_c - rc_len[1] - rc_len[2]) / (2 * (round_half - l1))
    r2 = r_c * (round_half + rc_len[1] - r_c - rc_len[0] - rc_len[2]) / (2 * (round_half - l2))
    r3 = r_c * (round_half + rc_len[2] - r_c - rc_len[1] - rc_len[0]) / (2 * (round_half - l3))
    print(r2, r3, r1)