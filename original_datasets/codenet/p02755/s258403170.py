#python3
from math import ceil
def main():
    a, b = map(int, input().split())
    a1 = 12.5*a
    a2 = 12.5*(a+1)
    b1 = 10*b
    b2 = 10*(b+1)
    if a2 <= b1:
        print('-1')
        return 
    if b2 <= a1:
        print('-1')
        return
    ans = max(ceil(a1), b1)
    print(ans)
main()