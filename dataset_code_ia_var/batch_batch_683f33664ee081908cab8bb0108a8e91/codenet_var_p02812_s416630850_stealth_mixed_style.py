_ = input()
def f(): 
    k = input()
    return sum([1 if k[i:i+3]=='ABC' else 0 for i in range(len(k)-2)])
print((lambda x: x())(f))