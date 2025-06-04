k = raw_input()
n = raw_input()
a = [int(i) for i in n.split()]
a.sort()
sum1 = 0
i = 0
while i < int(k):
    if a[2*i] < a[2*i+1]:
        sum1 += a[2*i]
    else:
        sum1 += a[2*i+1]
    i += 1
print sum1