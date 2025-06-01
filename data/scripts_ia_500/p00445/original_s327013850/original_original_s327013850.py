import sys
for e in sys.stdin:
 s=[e[i:i+3]for i in range(len(e)-3)]
 print(s.count('JOI'))
 print(s.count('IOI'))