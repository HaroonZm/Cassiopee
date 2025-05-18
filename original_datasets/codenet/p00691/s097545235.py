while 1:
	n3=mn=input()**3
	if n3==0:break
	i=0
	while 1:
		i+=1
		i3=i**3
		j=int((n3-i3)**(1/3.0))
		if j<i:break
		m=n3-i3-j**3
		if m<mn:mn=m
	print mn