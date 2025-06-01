def up(n):
	goal = [0 for i in range(n)]
	goal[:3] = [1,2,4]
	for i in range(3,n):
		goal[i] = sum(goal[i-3:i])
	return goal[-1]
	
while True:
	n = int(raw_input())
	if n == 0: break
	print (up(n)//10+1)//365+1