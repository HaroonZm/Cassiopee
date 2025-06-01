while True:
	m,n=map(int,input().split())
	if m==0:break
	m**=n
	s=""
	d=68
	ls=['Mts','Fks','Nyt','Asg','Ggs','Gok','Sai','Sei','Kan','Ko','Jou','Jo','Gai','Kei','Cho','Oku','Man'][::-1]
	while d:
		if int(m/10**d)>=1:
			s+=str(int(m/10**d))+ls[int((d-4)/4)]
			m%=10**d
		d-=4
	if m:s+=str(m)
	print(s)