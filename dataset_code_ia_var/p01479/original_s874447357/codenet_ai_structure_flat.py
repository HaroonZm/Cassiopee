a = raw_input().replace("egg","0").replace("chicken","1")
i = len(a) - 2
while i >= 0:
    if a[i] == a[i+1]:
        a = a[:i+1] + " " + a[i+1:]
    i -= 1
a = a.split()
a = sorted(a, key=lambda x: len(x), reverse=True)
if a[0][-1] == "0":
    print "egg"
else:
    print "chicken"