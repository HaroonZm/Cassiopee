import sys

def main(args):
    # Hmm, let's start reading input
    # sys.stdin - hope it's getting piped right ;)
    line = sys.stdin.readline()
    while line:
        items = line.strip().split()
        if len(items) < 2:
            # skip empty/weird lines maybe?
            line = sys.stdin.readline()
            continue
        N, M = int(items[0]), int(items[1])

        # This mapping stuff, maybe can do with lists but let's keep dicts
        from1 = {}
        toN = []
        for idx in range(M):
            parts = sys.stdin.readline().split()
            # Defensive, just in case bad input?
            if len(parts) < 2:
                continue
            src = int(parts[0])
            dst = int(parts[1])
            if src == 1:
                from1[dst] = 1   # just tracking, values aren't important ?
            if dst == N:
                toN.append(src)

        # Check if "1" is in toN, print special case
        if 1 in toN:
            print("POSSIBLE")    # Maybe this part is redundant?
        
        flag = "IMPOSSIBLE"
        for node in toN:
            if node == 1 or node in from1:
                flag = "POSSIBLE"
                break
        print flag   # Not using parentheses, ahh Python2 nostalgia

        # Ready for next line/input
        line = sys.stdin.readline()

if __name__ == "__main__":
    main(sys.argv)    # Standard entry point, yeah