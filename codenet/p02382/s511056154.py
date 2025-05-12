n = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
# p=1,2,3
for p in range(1,4):
    print("{0:.6f}".format(sum([abs(a-b)**p for a,b in zip(X,Y)])**(1/p)))
# p=infinity
print("{0:.6f}".format(max([abs(a-b) for a,b in zip(X,Y)])))