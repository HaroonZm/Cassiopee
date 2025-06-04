x = []
y = range(1, 14)

for val in y:
    x.append('S ' + str(val))
for val in y:
    x.append('H ' + str(val))
for val in y:
    x.append('C ' + str(val))
for val in y:
    x.append('D ' + str(val))

r = int(raw_input())
for i in range(r):
    card = raw_input()
    x.remove(card)

for card in x:
    print card