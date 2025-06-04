left = set("qwertasdfgzxcvb")
try:
    def transition(prev, curr):
        if prev == 0 and curr not in left:
            return 1
        elif prev == 1 and curr in left:
            return 1
        else:
            return 0
    import sys
    done = False
    while not done:
        s = raw_input()
        if "#"==s:
            done = True
            continue
        answer=0
        stat = None
        i=0
        while i < len(s):
            ch = s[i]
            if stat is None:
                stat = int(not (ch in left))
                i+=1
                continue
            answer += transition(stat, ch)
            stat ^= transition(stat, ch)
            i+=1
        print answer
except Exception as e: pass