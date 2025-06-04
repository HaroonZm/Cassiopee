while True:
    N = int(input())
    if N == 0:
        break

    marks = [input().strip() for _ in range(N)]

    # Parse marks
    # For each letter store: has_re, jump_type, jump_num
    letters = []
    for m in marks:
        if m == '-':
            letters.append({'has_re': False, 'jump_type': None, 'jump_num': None})
        else:
            has_re = 'v' in m
            if has_re:
                # jump mark + 'v'
                m0 = m[:-1]
            else:
                m0 = m
            # separate jump_type and jump_num if jump exists
            if has_re or (m0 != '' and m0 != 'v'):
                # find last digit start in m0
                i = len(m0) - 1
                while i >= 0 and m0[i].isdigit():
                    i -= 1
                i += 1
                if i < len(m0):
                    jump_type = m0[:i]
                    jump_num = int(m0[i:])
                else:
                    jump_type = None
                    jump_num = None
            else:
                jump_type = None
                jump_num = None
            letters.append({'has_re': has_re, 'jump_type': jump_type, 'jump_num': jump_num})

    read = [False] * N
    order = []

    # For tracking most recently read letter with jump_type and number 1
    last_read_jump1 = dict()

    # helper for next letter after k-th letter when jump is followed with no unread higher number
    def next_after(k):
        # next letter after index k (0-based)
        nxt = k + 1
        while nxt < N and read[nxt]:
            nxt += 1
        if nxt >= N:
            return None
        return nxt

    # find next letter with jump mark type t and number n that is unread and pos < pos_limit
    def find_unread_jump(t, n, pos_limit):
        for i in range(pos_limit):
            if not read[i]:
                l = letters[i]
                if l['jump_type'] == t and l['jump_num'] == n:
                    return i
        return None

    # find first unread letter starting from index s (0-based)
    def find_first_unread(s):
        i = s
        while i < N and read[i]:
            i += 1
        if i >= N:
            return None
        else:
            return i

    # Start reading

    # Because rule 2 says: letters with jump number >= 2 must be skipped at first reading
    # start from first letter (index 0), but if jump_num >= 2 skip it and start reading next unread letter

    # find first letter that can be read at start (not jump_num >= 2)
    current = 0
    while current < N:
        l = letters[current]
        if l['jump_num'] is not None and l['jump_num'] >= 2:
            # skip
            current += 1
        else:
            break
    if current >= N:
        # no letter found, no reading
        # but problem says one valid reading exists, so should not happen
        continue

    # read first letter
    read[current] = True
    order.append(current + 1)
    # update last_read_jump1
    l = letters[current]
    if l['jump_type'] is not None and l['jump_num'] == 1:
        last_read_jump1[l['jump_type']] = current

    # we keep track of previous letter index for rule 4
    prev = current

    # loop until no more letters can be read
    while True:
        next_letter = None

        # According to priority of the rules (last first to first):

        # 4. If current letter i read and previous letter (i-1) has 'Re' mark, then (i-1) must be read next.
        pre_idx = prev - 1
        if pre_idx >= 0 and not read[pre_idx]:
            if letters[pre_idx]['has_re']:
                next_letter = pre_idx

        # 3. When i-th letter with jump mark (t,n) read, and exists unread letter L with pos < i and jump mark (t,n+1), then L read next.
        if next_letter is None:
            l = letters[prev]
            if l['jump_type'] is not None and l['jump_num'] is not None:
                t = l['jump_type']
                n = l['jump_num']
                if n >= 1:
                    # look for unread letter L at position < prev with jump mark t and n+1
                    L = find_unread_jump(t, n + 1, prev)
                    if L is not None:
                        next_letter = L
                    else:
                        # If no such letter L, then (k+1)-th letter is read, where k is index of most recent letter with jump mark t,1 that was read.
                        if t in last_read_jump1:
                            k = last_read_jump1[t]
                            nidx = next_after(k)
                            if nidx is not None:
                                next_letter = nidx
                        else:
                            # if no such letter k, fallback to next letter after prev
                            nidx = next_after(prev)
                            if nidx is not None:
                                next_letter = nidx

        # 2. letter with jump mark number >= 2 must be skipped (if we directly try to read we skip)
        if next_letter is None:
            # just read next letter after prev that is not read and jump_num less than 2 or None
            nidx = next_after(prev)
            while nidx is not None and letters[nidx]['jump_num'] is not None and letters[nidx]['jump_num'] >= 2:
                nidx = next_after(nidx)
            if nidx is not None:
                next_letter = nidx
            else:
                next_letter = None

        # 1. Basically letters read top to bottom if no other applicable
        # Actually handled by finding next unread letter after prev above.

        # if no next_letter, end
        if next_letter is None:
            break

        # read next_letter
        read[next_letter] = True
        order.append(next_letter + 1)
        # update last_read_jump1 if applicable
        l = letters[next_letter]
        if l['jump_type'] is not None and l['jump_num'] == 1:
            last_read_jump1[l['jump_type']] = next_letter

        prev = next_letter

    for o in order:
        print(o)