import sys  # Importe le module sys, qui fournit l'accès à certaines variables et fonctions interagissant avec l'interpréteur Python.
from collections import deque  # Importe deque depuis le module collections, qui fournit une liste à double extrémité performante.

# Prend une ligne d'entrée utilisateur, la découpe en utilisant l'espace comme séparateur, 
# puis transforme chaque morceau en entier. Assigne ces deux entiers aux variables A et B respectivement.
A,B = map(int,input().split())

# Définit une fonction lambda nommé ask prenant deux paramètres x et y. 
# Cette fonction affiche la chaîne '?', suivie des valeurs de x et y, puis force l'affichage immédiat
# grâce à flush=True pour éviter la mise en tampon standard de l'affichage.
ask = lambda x,y: print('?',x,y, flush=True)

# Vérifie si la valeur de A est inférieure ou égale à celle de B.
if A <= B:
  # Si la condition précédente est vraie, affiche 'Impossible' immédiatement (en forçant le flush), 
  # puis termine le programme de manière prématurée en appelant sys.exit(), 
  # ce qui arrête l'exécution du script Python.
  print('Impossible', flush=True)
  sys.exit()

# Calcule la somme de A et B et l'assigne à la variable N.
N = A+B

# Crée un objet deque (file doublement enchaînée) contenant les entiers de 0 à N-1 inclus.
# Le second argument N sert de longueur maximale à la deque, limitant ainsi son nombre d’éléments à N.
candidates = deque(range(N), N)

# Démarre une boucle qui va continuer tant que le nombre d’éléments dans candidates est supérieur à 2.
while len(candidates) > 2:
  # Retire et retourne le dernier élément de la deque candidates, en l’assignant à x.
  x = candidates.pop()
  # Retire et retourne le nouvellement dernier élément, en l’assignant à y.
  y = candidates.pop()
  # Appelle la fonction ask avec x et y, affichant ainsi la question proposée à l'utilisateur ou à une entité.
  ask(x,y)
  # Lit une nouvelle ligne depuis l’entrée standard, qui est attendue être une réponse.
  # On vérifie si cette réponse est égale à la chaîne 'Y'.
  if input() == 'Y':
    # Si la condition est vraie (c’est-à-dire que la personne a répondu 'Y'), alors on ajoute y au début de la deque candidates.
    candidates.appendleft(y)
    # À ce stade, seuls les éléments jugés dignes au vu de la réponse survivent dans candidates.

# Après la boucle, il reste deux éléments dans candidates.
# Prend le premier élément de candidates et l’assigne à la variable god.
god = candidates[0]

# Initialise une liste vide nommée result, qui sera utilisée pour collecter des booléens.
result = []
# Démarre une boucle qui s’exécutera N fois, avec i prenant successivement toutes les valeurs comprises entre 0 et N-1 inclus.
for i in range(N):
  # À chaque itération, appelle la fonction ask avec god et i, affichant ainsi la question associant ces deux valeurs.
  ask(god,i)
  # Prend l'entrée utilisateur (on s'attend normalement à un 'Y' ou un 'N'),
  # compare la chaîne reçue à 'Y' pour produire True si c'est la même et False sinon,
  # puis ajoute ce booléen à la fin de la liste result.
  result.append(input() == 'Y')

# À la fin de la collecte des résultats, affiche une ligne commençant par le caractère '!' (qui signale la réponse finale),
# suivi de la concaténation des résultats sous forme de chaîne de chiffres 0 ou 1.
# Pour ce faire, on convertit chaque booléen de result en entier (int(True) donne 1 et int(False) donne 0),
# convertit ensuite chaque entier en chaîne de caractères, puis les joint en une seule chaîne (join).
# On s'assure enfin que l'affichage est immédiat via flush=True.
print('!', ''.join(str(int(s)) for s in result), flush=True)