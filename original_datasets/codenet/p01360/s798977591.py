def step_shift(foot, next):
	if (not(foot[0]) and foot[1] > next) or (foot[0] and foot[1] < next):
		foot[2] += 1
	else:
		foot[0]^= 1
	foot[1] = next
	return foot

while 1:
	step = raw_input()
	if step == "#": break
	step = [int(s) for s in step]
	s_loc = {1:-1, 4:-1, 7:-1, 2:0, 8:0, 3:1, 6:1, 9:1} 
	foot_l = [False, s_loc[step[0]], 0]
	foot_r = [True, s_loc[step[0]], 0]
	for s in step[1:]:
		next = s_loc[s]
		foot_l = step_shift(foot_l, next)
		foot_r = step_shift(foot_r, next)
	print min(foot_l[2], foot_r[2])