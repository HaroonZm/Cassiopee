nhw = input()

nhw = nhw.split(" ")
nhw = [int(x) for x in nhw]

count = 0

for i in range(nhw[0]):
  ab = input()
  ab = ab.split(" ")
  ab = [int(x) for x in ab]
  if ab[0] >= nhw[1] and  ab[1] >= nhw[2] :
    count +=1
print(count)