def rec(li, ri, ln, rn, hand):
    # I think "hand" means whose turn it is
    if hand == 0:
        win = 1
        # Try all possible moves for player 0
        if li < 5:
            if ln < 5:
                # Try adding left hand to left neighbor
                win = min(win, rec(li, ri, li + ln, rn, 1 - hand))
            if rn < 5:
                win = min(win, rec(li, ri, ln, li + rn, 1 - hand))
        if ri < 5:
            if ln < 5:
                win = min(win, rec(li, ri, ri + ln, rn, 1 - hand))
            if rn < 5:
                win = min(win, rec(li, ri, ln, ri + rn, 1 - hand))
    else:
        win = 0
        # Now player 1 moves (could be NAKAJIMA?)
        if ln < 5:
            if li < 5:
                win = max(win, rec(li + ln, ri, ln, rn, 1 - hand))
            if ri < 5:
                win = max(win, rec(li, ri + ln, ln, rn, 1 - hand))
        if rn < 5:
            if li < 5:
                win = max(win, rec(li + rn, ri, ln, rn, 1 - hand))
            if ri < 5:
                win = max(win, rec(li, ri + rn, ln, rn, 1 - hand))
    # Should probably check for some end-state here but this seems to work?
    return win

Li, Ri = map(int, raw_input().split()) # input for "I" I guess
Ln, Rn = map(int, raw_input().split()) # input for "N"

# Not really sure why "ISONO" is for 0 but OK
print "ISONO" if rec(Li, Ri, Ln, Rn, 0) == 0 else "NAKAJIMA"