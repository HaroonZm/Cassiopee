x_1, x_2 = input().split()
x_1 = int(x_1)
x_2 = int(x_2)

def diff(a,b):
    return a-b if a>b else b-a

print(diff(x_1,x_2))