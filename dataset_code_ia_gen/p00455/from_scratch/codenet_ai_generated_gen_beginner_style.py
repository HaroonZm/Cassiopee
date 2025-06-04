a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

def time_diff(start, end):
    sh, sm, ss = start
    eh, em, es = end
    # convertir en secondes
    start_sec = sh*3600 + sm*60 + ss
    end_sec = eh*3600 + em*60 + es
    diff = end_sec - start_sec

    h = diff // 3600
    diff = diff % 3600
    m = diff // 60
    s = diff % 60
    return h, m, s

ah, am, asec, ah2, am2, asec2 = a
bh, bm, bsec, bh2, bm2, bsec2 = b
ch, cm, csec, ch2, cm2, csec2 = c

ad = time_diff((ah, am, asec), (ah2, am2, asec2))
bd = time_diff((bh, bm, bsec), (bh2, bm2, bsec2))
cd = time_diff((ch, cm, csec), (ch2, cm2, csec2))

print(ad[0], ad[1], ad[2])
print(bd[0], bd[1], bd[2])
print(cd[0], cd[1], cd[2])