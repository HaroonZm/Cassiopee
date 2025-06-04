n=int(input())
total=n
COINS=(lambda: [1,5,10,25])()
steps=[0]

def eat(val,coin,remain):
    if not remain:
        return steps[0]
    x,a=divmod(val,coin)
    steps[0]+=x
    return a

flip=lambda l:l[::-1]

for z in flip(COINS):
    total=eat(total,z,total)
    if total==0: break

print(steps[0])