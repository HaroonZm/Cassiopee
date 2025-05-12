inputs = [input() for i in range(2)]
n = int(inputs[0])
a = map(lambda x: int(x), inputs[1].split(" "))

b = {}
for i in a:
  if i not in b:
    b[i] = 1
  else:
    b[i] += 1
count = 0
for k in b.keys():
  tmp = k - b[k]
  if tmp > 0:
    count += b[k]
  else:
    count += -tmp

print(count)