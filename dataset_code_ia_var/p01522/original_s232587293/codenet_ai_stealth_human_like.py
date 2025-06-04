# Okay, so, let's see... we have some input to read
n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])  # number of boats I guess?

# I think we gotta read each boat's members now
boats = []
for i in range(k):
    members = list(map(int, input().split()))
    # first element is the count, which we don't care about
    boats.append(set(members[1:]))

# then the number of "reports" or something
r = int(input())

out = set()
for i in range(r):
    stuff = input().split()
    p = int(stuff[0])
    q = int(stuff[1])
    for b in boats:  # I hope 'b' is a good enough name
        if p in b and q in b:
            out.add(p)
            out.add(q)
            break  # no need to check other boats

print((len(out)))  # Parens are maybe not needed but it's fine