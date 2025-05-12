n = int(raw_input())
a, b = map(float, raw_input().split(" "))
c = float(raw_input())

toppings = []
for i in range(n):
    toppings.append(float(raw_input()))

toppings.sort(cmp=(lambda x,y:cmp(y,x)))

cal_sum = c
doll_sum = a
for i in range(n):
    if cal_sum/doll_sum < (cal_sum+toppings[i])/(doll_sum+b):
        cal_sum += toppings[i]
        doll_sum += b
    else: break;

print int(cal_sum/doll_sum)