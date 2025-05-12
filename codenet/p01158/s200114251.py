import sys
sys.setrecursionlimit(10000) 

def checkloop(pdict,product,inroute,made):
    inroute.append(product)
    if pdict[product][1] in made:
        return (False,product)
    elif pdict[product][1]==product:
        return (False,product)
    elif pdict[product][1] in inroute:
        return (True,pdict[product][1])
    else:
        return checkloop(pdict,pdict[product][1],inroute,made)

def daysopen(pdict,product,made,notsearched):
    if pdict[product][1] in made:
        made.append(product)
        notsearched.remove(product)
        return pdict[product][2]
    if pdict[product][1]==product:
        made.append(product)
        notsearched.remove(product)
        return pdict[product][0]
    else:
        made.append(product)
        notsearched.remove(product)
        return daysopen(pdict,pdict[product][1],made,notsearched)+pdict[product][2]
    
def daysloop(pdict,product,made,notsearched,inloop):
    inloop.append(product)
    if pdict[product][1] in inloop:
       # print inloop
        smallestdifference=100000
        smallestdifferenceitem=""
        for item in inloop:
            if smallestdifference>pdict[item][0]-pdict[item][2]:
                smallestdifference=pdict[item][0]-pdict[item][2]
                smallestdifferenceitem=item
        #gotsmallestitem
        days=pdict[smallestdifferenceitem][0]
        made.append(smallestdifferenceitem)
        notsearched.remove(smallestdifferenceitem)
        inloop.remove(smallestdifferenceitem)
        for item in inloop:
            made.append(item)
            notsearched.remove(item)
            days=days+pdict[item][2]
        return days
    else:
        return daysloop(pdict,pdict[product][1],made,notsearched,inloop)
    
while(1):
    N=int(raw_input())
    if N==0:
        break
    else:
        pdict={}
        notsearched=[]
        notcomplete=1
        made=[]
        days=0
        for i in range(N):
            indat=raw_input().split()
            pdict[indat[0]]=(int(indat[1]),indat[2],int(indat[3])) #name=(d1,sup,d2)
            notsearched.append(indat[0])
        while len(notsearched)!=0:
            #check if loop
            inroute=[]
            product=notsearched[0]
            #check if sup made
            if pdict[product][1] in made:
                days=days+pdict[product][2]
                made.append(product)
                notsearched.remove(product)
            else:
                [loopbool,loopstartpoint]=checkloop(pdict,product,inroute,made)
                if loopbool:
                    inloop=[]
                    days=days+daysloop(pdict,loopstartpoint,made,notsearched,inloop)
                else:
                    days=days+daysopen(pdict,product,made,notsearched)
        print days