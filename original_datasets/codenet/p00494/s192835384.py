# AOJ 0571 JJOOII
# Python3 2018.6.20 bal4u

import re

pat = "(J*)(O*)(I*)"
ans = 0
for s in re.findall(pat, input()):
	j = len(s[0])
	o = len(s[1])
	i = len(s[2])
	if j >= o and i >= o: ans = max(ans, o)
print(ans)