n = int(raw_input())
for i in range(n):
	s = raw_input()
	length = len(s)
	organize_set = set([s, s[::-1]])
	for j in range(1,length):
		f = s[:j]
		frev = f[::-1]
		b = s[j:]
		brev = b[::-1] 
		organize_set.add(f + brev)
		organize_set.add(b + f)
		organize_set.add(brev + f)
		organize_set.add(frev + b)
		organize_set.add(frev + brev)
		organize_set.add(b + frev)
	print len(organize_set)