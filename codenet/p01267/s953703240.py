def Next(x) :
	return (A * x + B) % C

while True :
	N, A, B, C, X = map(int, input().split())
	if(C == 0) :
		break
	else :
		Y = list(map(int,input().split()))
		for i in range(10002) :
			if(i == 10001) :
				print(-1)
			else :
				if(X == Y[0]) :
					del Y[0]
				if(len(Y) == 0) :
					print(i)
					break
				else :
					X = Next(X)