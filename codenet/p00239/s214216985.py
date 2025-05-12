while True:
	n = input()
	if n == 0 : break

	calorieSet = []
	for _ in xrange(n):
		num,protein,lipid,carbohydrate = map(int,raw_input().split())
		sumCalorie = protein * 4 + carbohydrate * 4 + lipid * 9
		calorieSet.append((num, protein, lipid, carbohydrate, sumCalorie))
	
	limmit = map(int,raw_input().split())
	good = []
	for var in calorieSet:
		judge = True
		for cal,lim in zip(var[1:], limmit):
			if cal > lim:
				judge = False
				break
		if judge:
			good.append(var[0])
			
	if good == []:
		print "NA"
	else:
		for var in good:
			print var