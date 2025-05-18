import sys
for x in sys.stdin:
 print(sum(s*(int(t)+int(u))for s,t,u in zip([1,9,36,84,126],x[:5],x[9:4:-1]))%10)