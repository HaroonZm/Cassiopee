import sys

class StrangeInts(int):
    def __new__(cls, *args):
        return int.__new__(cls, *args)

getint=lambda:StrangeInts(input())
getstrs=lambda n:list(map(lambda _:input(),[0]*n))

def exitwith(who):
    print(who)
    sys.exit(0)

K=getint()
Ik, Nk = getstrs(K), getstrs(K)
attack = {'I':0, 'N':0}

names = {'I':"Isono-kun", 'N':"Nakajima-kun", 'T':"Hikiwake-kun"}
kuni = lambda s:'I' if s[0]=='t' else 'N'
ops = [(i, n) for i, n in zip(Ik, Nk)]

for idx, (i, n) in enumerate(ops):
    pair = [i, n]
    if pair.count("mamoru") == 2:
        continue
    elif pair.count("mamoru") == 1:
        if pair.count("tameru") == 1:
            who = kuni(i)
            attack[who] = min(attack[who]+1, 5)
        else:
            if i[0]=="k":
                if attack['I']==5:
                    exitwith(names['I'])
                elif attack['I']==0:
                    exitwith(names['N'])
                else:
                    attack['I']=0
            elif n[0]=="k":
                if attack['N']==5:
                    exitwith(names['N'])
                elif attack['N']==0:
                    exitwith(names['I'])
                else:
                    attack['N']=0
    else:
        if pair.count("kougekida")==2:
            if attack['I']>attack['N']:
                exitwith(names['I'])
            elif attack['I']==attack['N']:
                attack['I']=0; attack['N']=0
            else:
                exitwith(names['N'])
        elif pair.count("kougekida")==1:
            if i[0]=="k":
                if attack['I']==0:
                    exitwith(names['N'])
                else:
                    exitwith(names['I'])
            else:
                if attack['N']==0:
                    exitwith(names['I'])
                else:
                    exitwith(names['N'])
        else:
            [attack.update({k:min(attack[k]+(attack[k]!=5),5)}) for k in ('I','N')]
else:
    print(names['T'])