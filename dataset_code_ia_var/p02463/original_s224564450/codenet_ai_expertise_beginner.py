input()
L = input().split()
L2 = []
for x in L:
    L2.append(int(x))
input()
Q = input().split()
Q2 = []
for x in Q:
    Q2.append(int(x))
all_numbers = []
for x in L2:
    if x not in all_numbers:
        all_numbers.append(x)
for x in Q2:
    if x not in all_numbers:
        all_numbers.append(x)
all_numbers.sort()
for i in all_numbers:
    print(i)