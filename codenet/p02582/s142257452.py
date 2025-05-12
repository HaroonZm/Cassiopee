s = input()
r = s.count("RRR")
n = s.count("RR")

if r == 1:
    print(3)
elif n == 1:
    print(2)
else:
    if s.count("R")>0:
        print(1)
    else:
        print(0)