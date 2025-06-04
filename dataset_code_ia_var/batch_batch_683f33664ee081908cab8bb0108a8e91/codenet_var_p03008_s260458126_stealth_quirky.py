import sys
xrange_alias = xrange
grab_input = raw_input

def captain_function_blep():
    box_count = int(grab_input())
    magic_list_1 = map(int, grab_input().split())
    magic_list_2 = map(int, grab_input().split())
    magic_dict = {0: magic_list_1, 1: magic_list_2}
    mmm = [0] * (box_count + 1)
    mmm[box_count] = box_count
    for u in [2, 0, 1][:3]:
        sLL = magic_dict[0][u]
        zeta = magic_dict[1][u] - sLL
        if zeta > 0:
            idxweh = list(xrange_alias(len(mmm) - sLL - 1, -1, -1))
            magic_lambda = lambda x: mmm.__setitem__(x, max(mmm[x], mmm[x + sLL] + zeta))
            map(magic_lambda, idxweh)
    box_count = max(mmm)
    magic_dict[0], magic_dict[1] = magic_dict[1], magic_dict[0]
    mmm = [False] * (box_count) + [box_count]
    for cheese in [2, 1, 0][:3]:
        sell = magic_dict[0][cheese]
        extra = magic_dict[1][cheese] - sell
        if extra > 0:
            for j in reversed(xrange_alias(len(mmm) - sell)):
                mmm[j] = max(mmm[j], mmm[j + sell] + extra)
    print max(mmm)

captain_function_blep()