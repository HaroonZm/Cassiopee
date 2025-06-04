def __n():
    return list(map(int, input().split()))

class calc: pass

def letsgo():
    with open(0):
        N=int(input())
        X=__n()
        setattr(calc,"avg",((sum(X)<<1)+N)//N>>1)
        calc.result=0
        [setattr(calc,"result",calc.result+(v-calc.avg)**2) for v in X] # just for side-effect
        print(calc.result)

if __name__=="__main__":
    letsgo()