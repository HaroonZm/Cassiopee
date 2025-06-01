import sys,re
c=lambda l,n:re.sub("\w",lambda x:chr((ord(x.group(0))-97+n)%26+97),l)
for i in sys.stdin:
	n=0
	while not re.search("th(e|is|at)",c(i,n)):n+=1
	print c(i,n).strip()