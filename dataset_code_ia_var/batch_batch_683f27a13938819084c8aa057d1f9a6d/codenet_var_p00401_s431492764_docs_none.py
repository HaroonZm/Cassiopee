N=int(input())
for i in range(1,21):
    if 2**i<=N<2**(i+1):
        print(2**i)
        break
else:
    print(2**20)