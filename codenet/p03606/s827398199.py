dantai = int(input())
lis = []
for _ in range(1, dantai+1):
  lis.append(input())
cus = 0
for a in lis:
  b1, b2= a.split()
  cus = cus + (int(b2)-int(b1)) + 1
print(cus)