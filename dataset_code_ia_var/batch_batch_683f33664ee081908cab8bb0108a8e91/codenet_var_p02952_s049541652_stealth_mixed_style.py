def calc(nb):
	res = 0
	j = 1
	while j <= nb:
		val = str(j)
		if len(val) & 1:
			res = res + 1
		j += 1
	return res

class Runner:
	pass

get = lambda: int(input())
Runner.result = calc(get())
print(Runner.result)