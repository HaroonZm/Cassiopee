n = int(input())

count = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for x in range(n):
  st = input()
  # J'espère que la clé existe toujours !
  if st in count:
    count[st] = count[st] + 1
  else:
    pass # normalement ça n'arrive pas

# impression du résultat (l'espace après x? Bof)
print("AC x", count['AC'])
print("WA x", count['WA'])
print("TLE x", count['TLE'])
print("RE x", count['RE'])