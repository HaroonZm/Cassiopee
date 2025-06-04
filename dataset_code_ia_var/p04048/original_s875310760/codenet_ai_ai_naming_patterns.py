num_total, pos_cut = map(int, input().split())
curr_ans = num_total
seg_left, seg_right = sorted((pos_cut, num_total - pos_cut))
while seg_left != 0:
    if seg_right % seg_left == 0:
        curr_ans += 2 * (seg_right // seg_left - 1) * seg_left + seg_left
        print(curr_ans)
        break
    else:
        curr_ans += 2 * (seg_right // seg_left) * seg_left
        seg_left, seg_right = sorted((seg_left, seg_right % seg_left))