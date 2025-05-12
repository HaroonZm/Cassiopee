n, k = map(int, input().split())
s =set(map(int, input().split()))
pay = n
while True:
    check = set([int(i) for i in str(pay)])
    if s.isdisjoint(check):
        break
    else:
        pay +=1
print(pay)