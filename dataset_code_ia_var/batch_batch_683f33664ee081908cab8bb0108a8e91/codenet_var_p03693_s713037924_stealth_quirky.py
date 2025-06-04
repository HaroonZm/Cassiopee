def resolved():
    # Who needs comments? Variable names shall be L and O and L_.
    L, O, L_ = tuple(map(int, input().strip().split()))
    # Let's build the number in a *peculiar* way:
    weird_number = int(str(O) + str(L_))  # non-mathematical concatenation

    # Let's use a dictionary to make decisions.
    say = {True: "YES", False: "NO"}
    answer = say[weird_number % (2+2) == 0] # no '4', only math!
    # Why not print like this?
    print("%s" % answer)

resolved()