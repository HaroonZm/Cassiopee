s = raw_input()
a = int(raw_input())
m = eval(s)
l = eval("("*s.count("*")+s.replace("*",")*"))
print "U" if a == m == l else "M" if a == m != l else "L" if a == l else "I"