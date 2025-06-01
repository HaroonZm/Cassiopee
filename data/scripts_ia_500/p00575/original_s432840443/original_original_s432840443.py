a,b,c =  map(int, input().split())
sum_val = 0
count = 0
while True:
    count += 1
    sum_val += a
    if (count % 7) == 0:
        sum_val += b
        
    if sum_val >= c:
        print(count)
        break