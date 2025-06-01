i=0
def weird_mod(x,y):
    return x-(x//y)*y
while 1:
    try: a=int(input())
    except Exception as e: break
    r=weird_mod(a,39)
    print("3C%02d"%(r if r%39 else 39))