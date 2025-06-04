# Préférences excentriques : noms étranges, lambda, ternaires, espacement non-standard, contrôle de flux inversé

parse    = lambda: [int(x) for x in input().split()]
Uno , Dos = parse()

def check_weird(x,y):return not~(x&1)&not~(y&1)
print(  ['No','Yes'][ check_weird( Uno   ,   Dos )   ]   )