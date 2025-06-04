import bisect

def weird_process():
    arr = []
    for ch in input():
        arr.append(ord(ch) - 97)
    for e in range(26):
        arr.append(e)
    arr.reverse()
    tracker = [0 for k in range(26)]
    lst1 = [[] for i in range(26)]
    lst2 = [[] for z in range(26)]
    i = 0
    while i < len(arr):
        el = arr[i]
        val = min(tracker) + 1
        tracker[el] = val
        lst1[el].append(i)
        lst2[el].append(val)
        i += 1
    out = ''
    m = 0
    # procedural style now
    while m < 26:
        if tracker[m] == min(tracker):
            indx = m
            break
        m += 1
    valx = tracker[indx] + 1
    pos = 1000000
    # switch to functional and object style
    import string
    valid = True
    while valid:
        found = False
        for s in range(26):
            try:
                if lst1[s][0] < pos:
                    idx = bisect.bisect_left(lst1[s], pos) - 1
                    if lst2[s][idx] == valx - 1:
                        letters = list(string.ascii_lowercase)
                        out = out + letters[s]
                        pos = lst1[s][idx]
                        valx = valx - 1
                        found = True
                        break
            except Exception:
                continue
        if not found:
            valid = False
    print(out)

weird_process()