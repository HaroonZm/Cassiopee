import math
while(1):
    [p,n]=[int(x) for x in raw_input().split()]
    if p==0:
        break
    else:
       sqrtp=math.sqrt(p)
       smaller=[math.floor(sqrtp),int(math.floor(sqrtp)),1]
       larger=[math.ceil(sqrtp),int(math.ceil(sqrtp)),1]
       for numerator in range(int(math.floor(sqrtp))+1,n+1):
           denom_smaller=math.ceil(numerator/sqrtp)
           denom_larger=math.floor(numerator/sqrtp)
           if numerator/denom_smaller>smaller[0]:
               if smaller[1]*denom_smaller/smaller[2]!=numerator:
                   smaller=[numerator/denom_smaller,numerator,int(denom_smaller)]
           if numerator/denom_larger<larger[0]:
               if larger[1]*denom_larger/larger[2]!=numerator:
                   larger=[numerator/denom_larger,numerator,int(denom_larger)]
       print str(larger[1])+"/"+str(larger[2])+" "+str(smaller[1])+"/"+str(smaller[2])