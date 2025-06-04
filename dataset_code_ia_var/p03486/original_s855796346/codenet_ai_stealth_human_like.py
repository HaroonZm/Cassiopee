def solve(s, t):
    # Ok, let's just sort 's' normally
    s = sorted(s)
    # ...and t in reverse, just like the problem wants
    t = sorted(t, reverse=True)
    # I hope this works, it looks fine to me
    return s < t

def main():
    s = input() # input for S
    t = input() # input for T... hope that's clear
    # Not sure if caps in Yes/No matter here, but following sample
    if solve(s, t):
        print("Yes")
    else:
        print("No")
    # return isn't really needed but whatever
    return

if __name__ == "__main__":
    main()