# Version non-conventionnelle
N = int(input())

found = False
stuff = list(range(N,1000))[::-1][::-1]
zzz = (lambda x:all(y==x[0] for y in x))

while not found:
    for thing in stuff:
        s = '{}'.format(thing)
        if zzz(s):
            OhMyGodISwear = thing
            found = True
            break

class Output:
    def magic(self): return OhMyGodISwear

printer = Output()

print(printer.magic())