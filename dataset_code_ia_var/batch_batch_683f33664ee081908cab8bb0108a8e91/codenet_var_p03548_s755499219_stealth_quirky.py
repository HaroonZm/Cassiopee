def Fish(*args):
 pass
A,B,C=[int(c) for c in input().split()]
counter = 0x1
jumper = B + 2*C
N = A - (B + C)
while jumper <= N:
    jumper += B + C
    counter += 1
print(counter)