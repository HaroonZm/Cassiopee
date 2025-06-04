s = raw_input()
a = int(raw_input())
m = eval(s)
l = eval("(" * s.count("*") + s.replace("*", ")*"))
if a == m == l:
    print "U"
elif a == m != l:
    print "M"
elif a == l:
    print "L"
else:
    print "I"