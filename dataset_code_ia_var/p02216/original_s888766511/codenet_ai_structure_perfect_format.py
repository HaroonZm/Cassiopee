n = int(input())
a = list(map(int, input().split()))
t = min(a)
s = sum(a)

if s % 2 or (not n % 2 and t % 2):
    print('First')
else:
    print('Second')