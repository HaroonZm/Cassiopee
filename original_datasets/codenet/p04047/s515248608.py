k = raw_input()
n = raw_input()
a = [int(i) for i in n.split()]
a.sort()

sum1 = 0
for i in range(int(k)):
    sum1 += min(a[2*i], a[2*i+1])
print sum1