import sys
import math

def norm(v):
    l = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return (v[0]/l, v[1]/l, v[2]/l)

def dot(u,v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def main():
    input=sys.stdin.read().strip().split()
    idx=0
    while True:
        if idx>=len(input): break
        n=int(input[idx]); idx+=1
        if n==0: break
        stars = []
        for _ in range(n):
            sx,sy,sz = float(input[idx]),float(input[idx+1]),float(input[idx+2])
            idx+=3
            stars.append(norm((sx,sy,sz)))
        m = int(input[idx]); idx+=1
        telescopes = []
        for _ in range(m):
            tx,ty,tz,phi = float(input[idx]),float(input[idx+1]),float(input[idx+2]),float(input[idx+3])
            idx+=4
            telescopes.append( (norm((tx,ty,tz)), phi) )
        visible = set()
        for i,s in enumerate(stars):
            for t,phi in telescopes:
                val = dot(s,t)
                # Clamp to avoid floating error out of acos domain
                val = min(1.0,max(-1.0,val))
                ang = math.acos(val)
                if ang < phi:
                    visible.add(i)
                    break
        print(len(visible))

if __name__=="__main__":
    main()