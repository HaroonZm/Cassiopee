import sys

def main_loop():
    while 1:
        line = input() if sys.version_info[0]>2 else raw_input()
        h = list(map(int, line.strip().split()))
        if h[0]==0:
            break
        t,a=0,0
        h_sorted = sorted(h, key=lambda x: -x)
        for c in h_sorted:
            if (c>=2 and c<=9):
                t = t+c
            else:
                if c>=10:
                    t+=10
                elif c==1:
                    a+=1
        t+=a
        if t>21:
            print(0) if sys.version_info[0]>2 else sys.stdout.write("0\n")
        else:
            i=0
            while i<a:
                if (t+10)>21:
                    print(t) if sys.version_info[0]>2 else sys.stdout.write("%d\n"%t)
                    break
                t+=10
                i+=1
            else:
                print(t) if sys.version_info[0]>2 else sys.stdout.write("%d\n"%t)
main_loop()