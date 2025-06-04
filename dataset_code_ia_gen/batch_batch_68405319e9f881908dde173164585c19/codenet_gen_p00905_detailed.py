def count_brackets(line):
    # Count open and close brackets of each type in the line
    ro = line.count('(')
    rc = line.count(')')
    co = line.count('{')
    cc = line.count('}')
    so = line.count('[')
    sc = line.count(']')
    return ro, rc, co, cc, so, sc

def solve():
    import sys
    input = sys.stdin.readline
    while True:
        p, q = map(int, input().split())
        if p == 0 and q == 0:
            break

        P = [input().rstrip('\n') for _ in range(p)]
        Q = [input().rstrip('\n') for _ in range(q)]

        # Parse the P program lines:
        # For each line, record:
        # - indentation level (number of leading periods)
        # - incremental bracket counts (open and close)
        indent_levels = []
        ro_cum = [0]  # cumulative counts of open round brackets
        rc_cum = [0]  # cumulative counts of close round brackets
        co_cum = [0]  # cumulative counts of open curly brackets
        cc_cum = [0]  # cumulative counts of close curly brackets
        so_cum = [0]  # cumulative counts of open square brackets
        sc_cum = [0]  # cumulative counts of close square brackets

        for line in P:
            # count leading periods (indentation)
            indent = 0
            for ch in line:
                if ch == '.':
                    indent += 1
                else:
                    break
            indent_levels.append(indent)

            # count brackets in line
            ro, rc, co, cc, so, sc = count_brackets(line)
            ro_cum.append(ro_cum[-1] + ro)
            rc_cum.append(rc_cum[-1] + rc)
            co_cum.append(co_cum[-1] + co)
            cc_cum.append(cc_cum[-1] + cc)
            so_cum.append(so_cum[-1] + so)
            sc_cum.append(sc_cum[-1] + sc)

        # The first line has zero indentation in well-indented programs
        # Use the indentation formula:
        # indentation[line i] = R*(ro[i-1] - rc[i-1]) + C*(co[i-1] - cc[i-1]) + S*(so[i-1] - sc[i-1])
        # for i in 1..p-1 (0-based indexing; ro[i-1] means cumulative before line i)

        # We know indent_levels[i] for i in [0,p-1]
        # We want to find all possible triples (R,C,S) in [1..20]^3 that satisfy:
        # for i in range 1..p-1:
        #   indent_levels[i] == R*(ro_cum[i] - rc_cum[i]) + C*(co_cum[i] - cc_cum[i]) + S*(so_cum[i] - sc_cum[i])
        # First line indent_levels[0] == 0 must be satisfied by definition.

        candidates = []
        # Generate all possible triples of R,C,S in [1..20]
        for R in range(1, 21):
            for C in range(1, 21):
                for S in range(1, 21):
                    ok = True
                    for i in range(1, p):
                        expected = R*(ro_cum[i] - rc_cum[i]) + C*(co_cum[i] - cc_cum[i]) + S*(so_cum[i] - sc_cum[i])
                        if indent_levels[i] != expected:
                            ok = False
                            break
                    if ok:
                        candidates.append((R, C, S))

        # Now apply these candidates to Q lines:
        # For Q lines, compute cumulative brackets counts similarly,
        # then for each Q line i, calculate indentation candidates:
        # indentation_q[i] = R*(roq[i-1] - rcq[i-1]) + C*(coq[i-1] - ccq[i-1]) + S*(soq[i-1] - scq[i-1])
        #
        # If multiple candidate triples produce different indentation values for a given line, print -1 for that line
        # else print the unique indentation

        roq_cum = [0]
        rcq_cum = [0]
        coq_cum = [0]
        ccq_cum = [0]
        soq_cum = [0]
        scq_cum = [0]

        for line in Q:
            ro, rc, co, cc, so, sc = count_brackets(line)
            roq_cum.append(roq_cum[-1] + ro)
            rcq_cum.append(rcq_cum[-1] + rc)
            coq_cum.append(coq_cum[-1] + co)
            ccq_cum.append(ccq_cum[-1] + cc)
            soq_cum.append(soq_cum[-1] + so)
            scq_cum.append(scq_cum[-1] + sc)

        results = []
        for i in range(1, q+1):
            values = set()
            for R, C, S in candidates:
                indent_val = R*(roq_cum[i-1] - rcq_cum[i-1]) + C*(coq_cum[i-1] - ccq_cum[i-1]) + S*(soq_cum[i-1] - scq_cum[i-1])
                values.add(indent_val)
            if len(values) == 1:
                results.append(str(values.pop()))
            else:
                results.append(str(-1))

        print(' '.join(results))

if __name__ == '__main__':
    solve()