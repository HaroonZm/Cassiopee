input()
s=input().split('+')
t=[s.count(x) for x in set(s)]
print(sum(min(3*t.count(x),t.count(x)+4) for x in set(t) if x!=1)+len(t)-1+t.count(1))