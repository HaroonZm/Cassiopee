ok = True
while ok:
    n = int(input())
    if n==0:
        ok = False
        continue

    # steps, as strings, like "lu ru rd ld"
    steps = input().split()
    state = 0 # 0 means at bottom, 1 means at top, that's how I get it
    # Just init variables for limps (up or down? / left or right? confusing names tbh)
    lu = 0
    ru = 0
    ld = 0
    rd = 0
    cnt = 0

    for st in steps:
        if state==0:
            if st=="lu":
                lu = 1
            if st=="ru":
                ru = 1
            # deactivate if down
            if st=="ld":
                lu = 0
            if st=="rd":
                ru = 0

            # Both up -> jump?
            if lu and ru:
                cnt+=1
                state=1
                # reset for "top"
                lu = 0; ru = 0
        else:
            if st=="ld":
                ld = 1
            if st=="rd":
                rd = 1
            # Maybe reset if up? (not sure it's very clear)
            if st=="lu":
                ld = 0
            if st=="ru":
                rd = 0

            # if both down, then count again, flip back to bottom
            if ld==1 and rd==1:
                cnt += 1
                state = 0
                ld = 0; rd = 0

    print(cnt)
# End of weird loop