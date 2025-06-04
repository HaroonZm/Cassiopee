S = input()
# Extraction des caractères, style comprehensions
chars = list(S)

# Déclaration à l'ancienne façon C
evencount0, evencount1, unevencount0, unevencount1 = 0,0,0,0

# Alternance de styles fonctionnels et procéduraux
def count_even_odd(string):
    even0 = sum([1 for idx in range(1, len(string), 2) if string[idx]=='0'])
    even1 = (len(string)//2) - even0 if len(string)%2==0 else ((len(string)-1)//2) - even0
    odd0 = sum(map(lambda i: string[i]=='0', range(0, len(string), 2)))
    odd1 = ((len(string)+1)//2) - odd0 if len(string)%2 else (len(string)//2) - odd0
    return even0, even1, odd0, odd1

evencount0, evencount1, unevencount0, unevencount1 = count_even_odd(S)

elist = []
for v in (evencount0, evencount1, unevencount0, unevencount1):
    elist.append(v)

compare = lambda a, b: a if a > b else b

if compare(evencount1 + unevencount0, evencount0 + unevencount1) == evencount1 + unevencount0:
    k = evencount0 + unevencount1
else:
    k = evencount1 + unevencount0

print(k)