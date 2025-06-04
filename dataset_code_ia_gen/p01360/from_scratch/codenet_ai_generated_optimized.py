import sys

# Mapping arrows (1-9 except 5) to their horizontal positions (columns 1 to 3)
pos = {1:1, 2:2, 3:3,
       4:1,        6:3,
       7:1, 8:2, 9:3}

INF = 10**9

for line in sys.stdin:
    line=line.strip()
    if line == '#':
        break
    arrows = list(map(int, line))

    # dp[move index][left foot pos][right foot pos][last foot used (0=left,1=right)] = minimal violations
    # To optimize space and time, we store states as a dict: key=(lf,rf,foot), value=min violation
    # Initialize dp for first move: no violation, feet can start anywhere -> for first step, choose left or right freely
    dp = {}
    first = arrows[0]
    for lf in pos.keys():
        for rf in pos.keys():
            # Left foot presses first arrow
            if pos[first] >= pos[rf]:
                dp[(first, rf, 0)] = 0
            # Right foot presses first arrow
            if pos[first] <= pos[lf]:
                dp[(lf, first, 1)] = 0

    for i in range(1, len(arrows)):
        a = arrows[i]
        ndp = {}
        for (lf,rf,foot), val in dp.items():
            # Try next step with left foot
            # Left foot next position = a, must not be to the right of rf
            if pos[a] >= pos[rf]:
                nv = val + (1 if foot==0 else 0)
                key = (a, rf, 0)
                if key not in ndp or ndp[key] > nv:
                    ndp[key] = nv
            # Try next step with right foot
            # Right foot next position = a, must not be to the left of lf
            if pos[a] <= pos[lf]:
                nv = val + (1 if foot==1 else 0)
                key = (lf, a, 1)
                if key not in ndp or ndp[key] > nv:
                    ndp[key] = nv
        dp = ndp

    print(min(dp.values()))