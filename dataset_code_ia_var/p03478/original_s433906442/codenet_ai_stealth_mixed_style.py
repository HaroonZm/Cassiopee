n,a,b = (int(x) for x in input().split())
accumulator = 0
def digit_sum(val):
    s=0
    while val: s,val=s+val%10,val//10
    return s

i=1
while i<=n:
    t = digit_sum(i) if i%2 else sum(int(j) for j in str(i))
    if a<=t and t<=b:
        accumulator+=i
    i+=1

print(accumulator)