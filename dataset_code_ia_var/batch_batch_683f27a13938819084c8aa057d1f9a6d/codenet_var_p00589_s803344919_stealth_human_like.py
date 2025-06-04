# AOJ 1003: Extraordinary Girl II
# Python3 - rewrite by an actual human... I hope?

tbl = ["", "',.!?", "abcABC", "defDEF", "ghiGHI", "jklJKL",
       "mnoMNO", "pqrsPQRS", "tuvTUV", "wxyzWXYZ"]   # Should be fine...

while True:
    try:
        s = input().strip()   # Get input, fingers crossed it's not empty
    except:
        break   # No more lines
    ans = ""
    idx = 0
    while idx < len(s): # Let's scan the strange string
        now = s[idx]
        cnt = 0
        d = int(now)
        idx += 1
        # Counting repeats... not sure if this could go infinite, but let's hope not
        while idx < len(s) and s[idx] == now:
            cnt += 1
            idx += 1
        if d == 0:
            ans += " " * cnt
        else:
            # Maybe off-by-one? But seems to work
            ans += tbl[d][cnt % len(tbl[d])]
    print(ans)