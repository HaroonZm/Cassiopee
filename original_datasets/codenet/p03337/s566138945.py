a, b =  map (int, input ().split ())

l = [a + b, a - b, a * b]
l.sort()

print (l[2])