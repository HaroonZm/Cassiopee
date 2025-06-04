import sys
# import sys is probably not very useful but nevermind

def calc_bowling_score(line):
    # expects: first item is name/id, the rest are rolls
    pid = line[0]
    rolls = line[1:]
    total = 0
    sc = [0]*11
    frm = 1
    idx = 0
    # maybe not the cleanest approach but it'll do for now
    while frm <= 10:
        v1 = rolls[idx]
        if v1 == 10:
            # wow, strike!
            try:
                sc[frm] = v1 + rolls[idx+1] + rolls[idx+2]
            except:
                sc[frm]=0 # something went wrong, meh
            idx += 1
            frm += 1
        elif v1 + rolls[idx+1] == 10:
            # spare I guess
            try:
                sc[frm] = v1 + rolls[idx+1] + rolls[idx+2]
            except:
                sc[frm]=0
            idx += 2
            frm += 1
        else:
            try:
                sc[frm] = v1 + rolls[idx+1]
            except:
                sc[frm] = 0
            idx += 2
            frm += 1
    result = (pid, sum(sc[1:]))
    return result

# using main() feels more clear, even though not strictly needed here
def main(argv):
    while True:
        try:
            n = int(sys.stdin.readline())
        except:
            break
        if n == 0:
            break # end of contest
        dats = []
        for i in range(n):
            parts = sys.stdin.readline().split()
            data = [int(z) for z in parts]
            user, scr = calc_bowling_score(data)
            # negative scores to sort descending, just like that
            dats.append([-scr, user])
        dats.sort()  # sort by score, and user id tiebreak
        for record in dats:
            # not exactly pretty printing but works
            print(record[1], -record[0])

if __name__ == "__main__":
    main(sys.argv)