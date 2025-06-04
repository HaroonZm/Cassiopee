values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
import sys
for line in sys.stdin:
    s=line.strip()
    if not s:
        continue
    total=0
    for i in range(len(s)):
        val=values[s[i]]
        if i+1<len(s) and values[s[i+1]]>val:
            total-=val
        else:
            total+=val
    print(total)