A,B = [*map(int, input().split())]; total = sum([(lambda x: x==x[::-1])(str(num)) for num in range(A, B+1)])
print((lambda c: c)(total))