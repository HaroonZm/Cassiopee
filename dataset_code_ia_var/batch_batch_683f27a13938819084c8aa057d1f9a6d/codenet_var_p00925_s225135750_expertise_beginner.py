s = raw_input()
a = int(raw_input())
m = eval(s)

nb_etoiles = s.count("*")
l_temp = s.replace("*", ")*")
parentheses = "(" * nb_etoiles
l = eval(parentheses + l_temp)

if a == m == l:
    print "U"
elif a == m and m != l:
    print "M"
elif a == l:
    print "L"
else:
    print "I"