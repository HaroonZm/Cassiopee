N = int(input())

print((lambda x: (lambda y: y if y%2==0 else y*2)(x))(N))