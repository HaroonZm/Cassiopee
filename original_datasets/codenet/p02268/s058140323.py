_, s, _, t = [set(o.split()) for o in open(0)]
print(len(s & t))