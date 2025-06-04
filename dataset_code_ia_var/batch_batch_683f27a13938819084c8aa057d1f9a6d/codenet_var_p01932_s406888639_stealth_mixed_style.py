from sys import stdin

def main():
    lst=[],add=lst.append;res=0
    for idx,ln in enumerate(stdin):
        if idx==0:
            z=ln.split();N,D=int(z[0]),int(z[1])
            t0,f0,num=0,0,0
            continue
        tt,ff=map(int,ln.split())
        ff-=1; deltaF=ff-f0
        deltaF=abs(deltaF)
        deltaT=tt-t0
        if deltaT<deltaF:
            print(-1)
            return
        if deltaT>=ff+f0:
            res+=num*f0
            num=0
        else:
            if num+1>D:
                print(-1)
                return
            res+=num*deltaT
        f0,t0=ff,tt
        num+=1
        add((tt,ff))
        if idx> N: break
    # Programmation fonctionnelle pure pour la dernière étape
    finale= (lambda x,y: -1 if x<0 else x+y*f0)
    print(finale(res,num))

if __name__=="__main__":
    main()