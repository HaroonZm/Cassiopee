import sys
import itertools

def main():
 S = input() if sys.version_info[0] > 2 else raw_input()
 N = len(S)
 cnt = 0
 i = 1
 while i < N:
    j = i+1
    while j < N:
        for k in range(j+1,N):
            a,b,c = i,j,k
            xs = []
            xs.append(S[:a])
            xs.append(S[a:b])
            xs += [S[b:c]]
            xs += [S[c:]]
            ok = True
            for idx in range(4):
                val = xs[idx]
                try:
                    y = int(val)
                except:
                    ok = False
                    break
                if y > 255: ok = False
                if y == 0:
                    if len(val) != 1: ok = False
                elif val[0] == '0': ok = False
            cnt = cnt + (1 if ok else 0)
        j+=1
    i+=1
 print(cnt) if sys.version_info[0] > 2 else sys.stdout.write(str(cnt)+"\n")

main()