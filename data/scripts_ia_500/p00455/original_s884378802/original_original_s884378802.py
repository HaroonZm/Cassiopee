for _ in range(3):
	a = list(map(int, input().split()))
	wt = 3600*(a[3]-a[0])+60*(a[4]-a[1])+a[5]-a[2]
	print('{0} {1} {2}'.format(wt//3600, wt%3600//60, wt%3600%60))