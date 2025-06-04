n = input()
i = 0
while i < n:
    s = raw_input()
    s = s.replace("LL", "1")
    s = s.replace("UU", "1")
    s = s.replace("DD", "1")
    s = s.replace("RR", "1")
    if "1" in s:
        print "No"
    else:
        print "Yes"
    i += 1