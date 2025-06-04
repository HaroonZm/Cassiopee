X = int(input())
val = 100
for i in range(4000):
    val = (val*101)//100
    if val >= X:
        print(i+1)
        break