a_b = raw_input()
a_b_list = a_b.split()
a = int(a_b_list[0])
b = int(a_b_list[1])
if a < b:
    print "a < b"
elif a > b:
    print "a > b"
else:
    print "a == b"