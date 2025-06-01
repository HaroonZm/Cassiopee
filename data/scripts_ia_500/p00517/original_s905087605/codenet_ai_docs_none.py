cnt = 0
a, b, n = map(int, input().split())
w, h = map(int, input().split())
for i in range(1, n):
    mw, mh = map(int, input().split())
    if h < mh and w > mw or h > mh and w < mw:
        cnt += abs(mh - h) + abs(mw - w)
    else:
        cnt += max(abs(h - mh), abs(w - mw))
    w = mw
    h = mh
print(cnt)