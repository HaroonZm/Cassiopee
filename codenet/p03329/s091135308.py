y=int(input())

res=[]

for i in range(1,y+1):
	cnt=0
	y1=i
	y2=y-i

	for j in range(6,0,-1):
		t9=9**j
		if y1>=t9:
			cnt+=y1//t9
			y1=y1%t9
	y2+=y1

	for j in range(7,0,-1):
		t6=6**j
		if y2>=t6:
			cnt+=y2//t6
			y2=y2%t6

	cnt+=y2
	res.append(cnt)

print(min(res))