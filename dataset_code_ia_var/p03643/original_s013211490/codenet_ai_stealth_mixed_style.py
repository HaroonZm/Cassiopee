def concat():
    import sys
    res = "ABC"
    user = None
    for line in sys.stdin:
        user = line.rstrip()
        break
    print("{}{}".format(res, user if user is not None else ""))

concat()