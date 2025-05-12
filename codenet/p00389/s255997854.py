n, k = map(int, input().split())
weight = 1
rest = n - 1
layers = 1
while True:
  add = weight // k + bool(weight % k)
  if add <= rest:
    rest -= add
    weight += add
    layers += 1
  else:
    break
print(layers)