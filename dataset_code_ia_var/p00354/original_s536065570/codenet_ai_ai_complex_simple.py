import itertools, operator

jours=lambda:dict(enumerate(itertools.islice(itertools.cycle(['thu','fri','sat','sun','mon','tue','wed']),7)))
indice=lambda:operator.mod(int(input()),7)
print(jours()[indice()])