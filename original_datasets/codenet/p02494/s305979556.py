#!/opt/local/bin/python
while 1:
	a = map(int,raw_input().split())
	if a[0]==0 and a[1]==0:
		break
	for b in range(a[0]):
		print"#"*a[1]
	else:print