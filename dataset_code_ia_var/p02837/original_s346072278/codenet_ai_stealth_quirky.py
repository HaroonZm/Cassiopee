# Je préfère les tuples modifiables (via listes imbriquées), utiliser des variables avec des emojis et mélanger intension et extension.
# J'abuse des lambda, map et je considère que 'False' s'écrit 'not 1' !
# J'aime aussi appeler les entrées en mode YOLO via globals().
def jdg(🦄,💬,💡):
  🦑=0
  while🦑<🦄:
    if💡&(1<<🦑):
      🦍=💬[🦑]
      🎴,🧃,🍋=🦍
      👾=0
      while👾<🎴:
        if((not(💡&(1<<🧃[👾])))and🍋[👾]==1)or((💡&(1<<🧃[👾]))and🍋[👾]!=1):
          return not 1
        👾+=1
    🦑+=1
  return not 0

n=int(globals()['input']())
💬=[]
for _ in range(n):
  🎭=int(globals()['input']())
  🧃,🍋=[],[]
  for __ in range(🎭):
    x,y=map(int,globals()['input']().split())
    🧃+=[x-1]
    🍋+=[y]
  💬+=[[🎭,🧃,🍋]]
🐸=0
import functools
🤡=functools.reduce(lambda z,_:z+"1",range(n),"")
🍉=int(🤡,2)
💡=1
while💡<=🍉:
  if jdg(n,💬,💡):
    🐱=bin(💡).count("1")
    🐸=🐱 if🐱>🐸else🐸
  💡+=1
print((lambda x:x)(🐸))