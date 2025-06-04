from itertools import accumulate as acc

def main():
    get = lambda: list(map(int, input().split()))
    pop = None
    while True:
        *cdwx, = get()
        c, d, w, x = cdwx
        if not c: return
        es, fs = {}, {}
        for z in range(d): es[z] = []
        for z in range(c):
            for k, val in enumerate(get()):
                es[k].append(val)
        for z in range(d): fs[z] = []
        for z in range(c):
            for k, val in enumerate(get()):
                fs[k].append(val)
        for day in es:
            for i, v in enumerate(es[day]):
                if not v: fs[day][i] = 100
        for arr in (es, fs):
            for idx in arr: arr[idx] = [0] + list(acc(arr[idx]))
        superdict1, superdict2 = {}, {}
        for day in range(d):
            ls1, ls2 = [(0,0)], []
            for i in range(c):
                for j in range(i+1, c+1):
                    delta_f = fs[day][j] - fs[day][i]
                    delta_e = es[day][j] - es[day][i]
                    if delta_f <= w:
                        if j-i==1: ls1.append((delta_f,delta_e))
                        else: ls2.append((delta_f,delta_e))
            superdict1[day] = ls1
            superdict2[day] = ls2
        for dct in (superdict1, superdict2):
            for day in dct:
                seen = {}
                for f, e in dct[day]:
                    seen[f] = max(e, seen.get(f,-99999))
                dct[day] = sorted(seen.items())
        pog = [[[pop for _ in range(x+1)] for _ in range(w+1)] for _ in range(d+1)]
        pog[0][0][0] = 0
        for day in range(d):
            for weight in range(w+1):
                for use in range(x+1):
                    val = pog[day][weight][use]
                    if val is pop: continue
                    for f, e in superdict1[day]:
                        nxt = weight+f
                        if nxt > w: break
                        nv = pop if pog[day+1][nxt][use] is pop else pog[day+1][nxt][use]
                        if nv is pop or nv < val+e:
                            pog[day+1][nxt][use]=val+e
                    if use>=x: continue
                    for f, e in superdict2[day]:
                        nxt = weight+f
                        if nxt > w: break
                        nv = pop if pog[day+1][nxt][use+1] is pop else pog[day+1][nxt][use+1]
                        if nv is pop or nv < val+e:
                            pog[day+1][nxt][use+1]=val+e
        ans = 0
        for W in range(w+1):
            for R in range(x+1):
                z = pog[d][W][R]
                if z is not pop: ans = max(ans,z)
        print(ans)
main()