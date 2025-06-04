while True:
    N = input()
    if N == '0':
        break
    N = int(N)
    a = input().split()
    broken_positions = []
    known_values = {}
    for i in range(N):
        if a[i] == 'x':
            broken_positions.append(i)
        else:
            known_values[i] = int(a[i])

    if len(broken_positions) == 0:
        # Check if given signal satisfies condition
        ok = True
        for i in range(N):
            if i % 2 == 0:
                # odd indexed sample (1-based) i.e. i even zero-based index
                if i > 0 and not (known_values[i] < known_values.get(i-1, known_values[i])):
                    ok = False
                    break
                if i < N-1 and not (known_values[i] < known_values.get(i+1, known_values[i])):
                    ok = False
                    break
            else:
                # even indexed sample (1-based)
                if i > 0 and not (known_values[i] > known_values.get(i-1, known_values[i])):
                    ok = False
                    break
                if i < N-1 and not (known_values[i] > known_values.get(i+1, known_values[i])):
                    ok = False
                    break
        if ok:
            print('ambiguous')
        else:
            print('none')
        continue

    # Try all possible candidate values from -10**9 to 10**9 (not feasible to try all in beginner style)
    # Instead, try all distinct values observed plus one extra outside the range as candidates

    # Gather candidate values:
    candidates = set()
    for v in known_values.values():
        candidates.add(v)
        candidates.add(v-1)
        candidates.add(v+1)
    candidates.add(-10**9)
    candidates.add(10**9)

    possible_values = []
    for val in candidates:
        # try val as broken sample value
        new_signal = []
        for i in range(N):
            if i in broken_positions:
                new_signal.append(val)
            else:
                new_signal.append(known_values[i])
        # check constraints
        ok = True
        for i in range(N):
            if i % 2 == 0:
                if i > 0 and not (new_signal[i] < new_signal[i-1]):
                    ok = False
                    break
                if i < N-1 and not (new_signal[i] < new_signal[i+1]):
                    ok = False
                    break
            else:
                if i > 0 and not (new_signal[i] > new_signal[i-1]):
                    ok = False
                    break
                if i < N-1 and not (new_signal[i] > new_signal[i+1]):
                    ok = False
                    break
        if ok:
            possible_values.append(val)

    if len(possible_values) == 0:
        print('none')
    elif len(possible_values) == 1:
        print(possible_values[0])
    else:
        print('ambiguous')