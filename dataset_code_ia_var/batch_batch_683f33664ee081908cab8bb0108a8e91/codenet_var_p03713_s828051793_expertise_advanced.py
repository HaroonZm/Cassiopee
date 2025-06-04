from sys import stdin
from math import inf

H, W = map(int, stdin.readline().split())

def calc_ans(H, W):
    ans = inf

    for h in range(1, H):
        area_a = h * W
        remaining_h = H - h

        # 最適化: 事前計算
        for split_w in [W // 2]:
            area_b2 = remaining_h * split_w
            area_c2 = remaining_h * (W - split_w)
            area_list2 = (area_a, area_b2, area_c2)
            ans = min(ans, max(area_list2) - min(area_list2))

        rem_h_half = remaining_h // 2
        area_b1 = rem_h_half * W
        area_c1 = (remaining_h - rem_h_half) * W
        area_list1 = (area_a, area_b1, area_c1)
        ans = min(ans, max(area_list1) - min(area_list1))

    for w in range(1, W):
        area_a = w * H
        remaining_w = W - w

        for split_h in [H // 2]:
            area_b2 = remaining_w * split_h
            area_c2 = remaining_w * (H - split_h)
            area_list2 = (area_a, area_b2, area_c2)
            ans = min(ans, max(area_list2) - min(area_list2))

        rem_w_half = remaining_w // 2
        area_b1 = rem_w_half * H
        area_c1 = (remaining_w - rem_w_half) * H
        area_list1 = (area_a, area_b1, area_c1)
        ans = min(ans, max(area_list1) - min(area_list1))

    print(ans)

calc_ans(H, W)