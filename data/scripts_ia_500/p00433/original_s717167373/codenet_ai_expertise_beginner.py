import sys
f = sys.stdin

line1 = f.readline()
numbers1 = line1.split()
sum1 = int(numbers1[0]) + int(numbers1[1])

line2 = f.readline()
numbers2 = line2.split()
sum2 = int(numbers2[0]) + int(numbers2[1])

if sum1 >= sum2:
    print(sum1)
else:
    print(sum2)