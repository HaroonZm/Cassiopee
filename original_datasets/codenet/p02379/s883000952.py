import math
a,b,c,d=(float(x) for x in input().split())

l=(math.sqrt((a-c)*(a-c)+(b-d)*(b-d)))

print('{:.08f}'.format(l))