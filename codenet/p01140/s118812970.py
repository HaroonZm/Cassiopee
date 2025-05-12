while 1 :
	n, m = map(int,raw_input().split(" "))
	if (n, m) == (0,0):
		break
	Lon = [0 for i in range(1000 * n + 1)]
	Lat = [0 for i in range(1000 * m + 1)]
	Lon_sum = [0 for i in range(n)]
	Lat_sum = [0 for i in range(m)]
	for i in range(0,n):
		h = int(raw_input())
		for j in range(i+1):
			Lon_sum[j] += h
			Lon[Lon_sum[j]] += 1
	for i in range(0,m):
		tmp_Lat_sum = [0]
		w = int(raw_input())
		for j in range(i+1):
			Lat_sum[j] += w
			Lat[Lat_sum[j]] += 1
	max_width = min(Lon_sum[0],Lat_sum[0])
	print sum([Lon[i]*Lat[i] for i in range(1,max_width+1)])