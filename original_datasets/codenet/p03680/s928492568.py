N = int(input())
dic = {}
for i in range(N):
  a = int(input())
  dic[i+1] = a
counter = 0
place = 1
while place != 2:
  if dic[place] in dic and dic[place] != place:
    temp = dic[place]
    dic.pop(place)
    place = temp
    counter += 1
  else:
    counter = -1
    break
print(counter)