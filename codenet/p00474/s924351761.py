def loadIcicle():
	icicles = []
	line = input().strip().split(" ")
	N, L = int(line[0]), int(line[1])
	while True:
		icicles.append(int(input().strip()))
		if len(icicles) == N: break
	return icicles, N, L

def calcDiff(icicles, N):
	diff_2times = [0]*N

	for idx in range(N):
		dif_right = icicles[idx+1] - icicles[idx] if idx != N-1 else -icicles[idx]
		dif_left = icicles[idx] - icicles[idx-1] if idx != 0 else icicles[idx]

		dif_right = 1 if dif_right > 0 else -1
		dif_left = 1 if dif_left > 0 else -1

		if dif_right - dif_left < 0: diff_2times[idx] = -1
		elif dif_right - dif_left > 0: diff_2times[idx] = 1
		else: diff_2times[idx] = 0

	return diff_2times

icicles, N, L = loadIcicle()
diff_2times = calcDiff(icicles, N)

time = [-1]*N
peakX = [i for i in range(N) if diff_2times[i]==-1]
for i in peakX:
	time[i] = L - icicles[i]

	isLocalMinL, isLocalMinR = False, False
	posL, posR = i, i
	while not (isLocalMinL and isLocalMinR):
		posL -= 1
		if posL < 0:
			isLocalMinL = True
		if not isLocalMinL:
			if time[posL] == -1:
				time[posL] = (L-icicles[posL]) + time[posL+1]
			else:
				time[posL] = (L-icicles[posL]) + max(time[posL-1], time[posL+1])

			if diff_2times[posL] == 1:
				isLocalMinL = True

		posR += 1
		if posR >= N:
			isLocalMinR = True
		if not isLocalMinR:
			if time[posR] == -1:
				time[posR] = (L-icicles[posR]) + time[posR-1]
			else:
				time[posR] = (L-icicles[posR]) + max(time[posR-1], time[posR+1])

			if diff_2times[posR] == 1:
				isLocalMinR = True

print(max(time))