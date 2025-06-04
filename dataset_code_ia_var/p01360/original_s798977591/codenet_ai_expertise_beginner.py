def step_shift(foot, next):
    if (foot[0] == False and foot[1] > next) or (foot[0] == True and foot[1] < next):
        foot[2] = foot[2] + 1
    else:
        if foot[0]:
            foot[0] = False
        else:
            foot[0] = True
    foot[1] = next
    return foot

while True:
    step = raw_input()
    if step == "#":
        break
    step = [int(s) for s in step]
    s_loc = {1: -1, 4: -1, 7: -1, 2: 0, 8: 0, 3: 1, 6: 1, 9: 1}
    foot_l = [False, s_loc[step[0]], 0]
    foot_r = [True, s_loc[step[0]], 0]
    for s in step[1:]:
        next = s_loc[s]
        foot_l = step_shift(foot_l, next)
        foot_r = step_shift(foot_r, next)
    if foot_l[2] < foot_r[2]:
        print foot_l[2]
    else:
        print foot_r[2]