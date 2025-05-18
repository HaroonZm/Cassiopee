n=input()
a=set(map(int, input().split()))
m=input()
b=set(map(int, input().split()))
c={print(x) for x in sorted(set(a&b))}