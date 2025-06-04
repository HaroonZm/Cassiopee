lines = open(0).readlines()
a = lines[1:]
found_odd = False
for b in a:
    if int(b) % 2 != 0:
        found_odd = True
if found_odd:
    print("first")
else:
    print("second")