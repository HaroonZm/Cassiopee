M=list(range(1,31))
for i in range (28):
    S=int(input())
    M.remove(S)
print(min(M))
print(max(M))