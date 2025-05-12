def calc(n):
    if n%2==0:
        return int(n/2)
    else:
        return int(3*n+1)

s = int(input())

num = [s]
count = 0
while True:
    
    ans = calc(num[count])
    if ans in num:
        print(count+2)
        break
    num.append(ans)
    count += 1