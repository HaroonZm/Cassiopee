for _ in range(input()):
    step = raw_input()
    step = step.replace("LL", "1")
    step = step.replace("UU", "1")
    step = step.replace("DD", "1")
    step = step.replace("RR", "1")
    if "1" in step:
        print "No"
    else:
        print "Yes"