x,a,b = map(int, input().split())
if abs(a-x) < abs(b-x):
    print("A")
elif abs(b-x) < abs(a-x):
    print("B")