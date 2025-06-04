p = raw_input()

if len(p) < 6:
    print "INVALID"
elif p.islower():
    print "INVALID"
elif p.isupper():
    print "INVALID"
elif p.isalpha():
    print "INVALID"
elif p.isdigit():
    print "INVALID"
else:
    print "VALID"