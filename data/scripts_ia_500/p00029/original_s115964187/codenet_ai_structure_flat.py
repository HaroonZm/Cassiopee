a=raw_input().split()
dawa=''
d_count=0
d_word=''
for w in a:
	if len(w)>len(dawa):
		dawa=w
	count=a.count(w)
	if count>d_count:
		d_count=count
		d_word=w
print '%s %s' % (d_word,dawa)