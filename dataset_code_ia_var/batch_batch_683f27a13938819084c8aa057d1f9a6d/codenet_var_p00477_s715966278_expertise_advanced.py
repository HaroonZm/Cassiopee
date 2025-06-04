from functools import reduce

times = map(int, (input() for _ in range(4)))
total = reduce(int.__add__, times)
mins, secs = divmod(total, 60)
print(mins)
print(secs)