n = int(input())
l = len(bin(n)) - 1
print(2 ** (l - int(bin(n).find("1"))))