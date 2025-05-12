n = int(input())
ng = 0
def prime(a):
    if a == 1: return 1
    i = 3
    while i <= a / i:
        if a % i == 0:
            return 0
        i += 2
    return 1

for i in range(n):
    a = 2 * int(input()) + 1
    ng += prime(a)
    
print(ng)