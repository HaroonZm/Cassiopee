C = []
for i in range(5):
    X = int(input())
    if X < 40:
        X = 40
    C.append(X)
    
print((sum(C))//5)