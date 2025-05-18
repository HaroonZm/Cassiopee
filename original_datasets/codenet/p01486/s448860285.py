import re
b=s=input()
while 1:
    s=re.sub(r'(m|e)mew(e|w)','\\1\\2',s)
    if b==s:break
    b=s
print(['Rabbit','Cat'][s=='mew'])