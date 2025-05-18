import sys
for e in sys.stdin:
 s=sum((e[i:i+3]=='JOI')+1j*(e[i:i+3]=='IOI')for i in range(len(e)-3))
 print(int(s.real))
 print(int(s.imag))