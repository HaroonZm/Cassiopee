N = int(input())

i = 1
while True:
    if 2**i <= N < 2**(i+1):
        print(2**i)
        break
    i += 1
    if i > 20:
        print(2**20)
        break