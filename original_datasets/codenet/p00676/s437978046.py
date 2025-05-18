import math
while True:
    try:
        a,l,x=map(int,raw_input().split())
    except EOFError:
        break

    ANS=math.sqrt(pow(l,2)-pow(a/2.0,2))*a/2+math.sqrt(pow((l+x)/2.0,2)-pow(l/2.0,2))*l/2*2
    print ANS