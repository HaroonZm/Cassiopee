a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])

add = a + b
sub = a - b
mul = a * b

if add >= sub and add >= mul:
    print(add)
elif sub >= add and sub >= mul:
    print(sub)
else:
    print(mul)