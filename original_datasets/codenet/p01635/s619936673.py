n,T=map(int,raw_input().split())
f=raw_input()
t=eval(f.replace("^","**"))*T
print t if t<=pow(10,9) else "TLE"