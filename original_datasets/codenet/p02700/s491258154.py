A,B,C,D = map(int, input().split())

t = (A+D-1)//D
a = (C+B-1)//B
if t >= a:
    print("Yes")
else:
    print("No")