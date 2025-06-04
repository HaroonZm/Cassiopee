N = int(input())
print(len(bin(N))-2 if N > 0 else 0)