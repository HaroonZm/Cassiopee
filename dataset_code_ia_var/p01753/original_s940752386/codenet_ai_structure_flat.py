eps = 1.0 / 10**10
arr = input().split()
n = int(arr[0])
q = int(arr[1])
idx = 2
na = []
for _ in range(n):
    na.append([int(arr[idx]), int(arr[idx+1]), int(arr[idx+2]), int(arr[idx+3]), int(arr[idx+4])])
    idx += 5
qa = []
for _ in range(q):
    qa.append([int(arr[idx]), int(arr[idx+1]), int(arr[idx+2]), int(arr[idx+3]), int(arr[idx+4]), int(arr[idx+5])])
    idx += 6
rr = []
for qv in qa:
    x1, y1, z1, x2, y2, z2 = qv
    tr = 0
    for nv in na:
        x, y, z, r, l = nv
        a = (x1, y1, z1)
        b = (x2, y2, z2)
        c = (x, y, z)
        ab = ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) ** 0.5
        ac = ((a[0]-c[0])**2 + (a[1]-c[1])**2 + (a[2]-c[2])**2) ** 0.5
        bc = ((b[0]-c[0])**2 + (b[1]-c[1])**2 + (b[2]-c[2])**2) ** 0.5
        ok = False
        if ac <= r or bc <= r:
            ok = True
        else:
            at = (ac ** 2 - r ** 2) ** 0.5
            bt = (bc ** 2 - r ** 2) ** 0.5
            if ab >= at + bt - eps:
                ok = True
        if ok:
            tr += l
    rr.append(tr)
print('\n'.join(str(x) for x in rr))