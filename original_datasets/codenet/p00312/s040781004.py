ins = [int(x) for x in input().split()]

if ins[0] < ins[1]:
    print(ins[0])
else:
    print(int(ins[0]/ins[1])+int(ins[0]%ins[1]))