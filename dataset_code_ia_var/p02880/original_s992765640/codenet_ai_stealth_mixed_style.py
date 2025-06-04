N = int(input())
seq = []
for j in range(1, 10): seq.append(j)
i = 0
found = False
while i < len(seq):
    el = seq[i]
    if not N % el:
        q = N // el
        if q in seq:
            print("Yes")
            found = True
            break
    i += 1
if not found:
    print("No")