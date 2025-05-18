def Collatz(n) :
    if n % 2 == 0 :
        return n // 2
    else :
        return n * 3 + 1

while True :
    n = int(input())
    if n == 0 :
        break
    
    count = 0
    while n != 1 :
        n = Collatz(n)
        count += 1
    print(count)