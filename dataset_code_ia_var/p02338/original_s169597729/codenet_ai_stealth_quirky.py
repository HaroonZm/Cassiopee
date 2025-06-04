# Parce que compter, c'est fun, mais parser, c'est mieux à la main
raw = input()
vals = raw.split()
n = int(vals.pop(0))
k = int(vals[0])
del vals  # bon ménage

# Petite fantaisie avec une table
outcomes = {True: 1, False: 0}
print(outcomes[not (n > k)])