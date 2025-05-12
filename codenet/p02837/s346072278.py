#include <bitset>

def judge(n, testimony, hypothesis):
    i = 0
    while i < n:
        if hypothesis & (1 << i):
            a, xlist, ylist = testimony[i]
            
            j = 0
            while j < a:                
                if (not (hypothesis & (1 << xlist[j])) and ylist[j] == 1) \
                    or ((hypothesis & (1 << xlist[j])) and ylist[j] != 1):
                    return False

                j += 1

        i += 1
    
    return True

# input
n = int(input())

i = 0
testimony = []
while i < n:
    a = int(input())
    xlist = []
    ylist = []

    j = 0
    while j < a:
        x, y = map(int, input().split())
        xlist.append(x - 1)
        ylist.append(y)

        j += 1

    tlist = [a, xlist, ylist]
    testimony.append(tlist)

    i += 1

# processing
num = 0

i = 0
bstr = ""
while i < n:
    bstr += "1"
    i += 1

b = int(bstr, 2)

hypothesis = 0b1
while hypothesis <= b:
    if judge(n, testimony, hypothesis):
        tnum = bin(hypothesis).count("1")
        if num < tnum:
            num = tnum

    hypothesis += 1

# output
print(num)