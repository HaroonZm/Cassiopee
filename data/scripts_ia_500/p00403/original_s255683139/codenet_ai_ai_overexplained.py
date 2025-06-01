# Initialisation de la liste 'cats' avec 101 éléments tous initialisés à 0.
# Cette liste va servir à suivre l'état (présence ou absence) de 100 chats numérotés de 1 à 100.
# L'indice 0 n'est pas utilisé.
cats = [0 for i in range(101)]

# Initialisation d'une pile vide (liste Python utilisée comme une pile).
# Cette pile va servir à garder la trace des chats actuellement "à l'intérieur".
stack = []

# Lecture d'un entier depuis l'entrée standard.
# Cet entier représente le nombre total d'actions qui seront traitées.
L = int(input())

# Lecture d'une ligne de texte depuis l'entrée standard, puis découpage de cette ligne en éléments.
# Chaque élément est converti en entier pour former la liste 'c'.
# Cette liste 'c' contient les actions sur les chats à traiter : 
# un entier positif signifie qu'un chat entre, un entier négatif qu'un chat sort.
c = [int(i) for i in input().split()]

# Initialisation de la variable 'ans' avec la valeur -1.
# Cette variable servira à stocker la position (index + 1) de la première action invalide détectée.
# Si aucune action invalide n'est trouvée, 'ans' restera à -1.
ans = -1

# Boucle à travers chaque action de la liste 'c' en utilisant son indice 'i'.
for i in range(L):
    # Ici, on traite l'action actuelle, qui est c[i].

    # Si l'action est un entier positif (> 0), cela signifie qu'un chat entre.
    if c[i] > 0:
        # Vérifions si le chat avec l'identifiant c[i] est déjà dans la maison.
        # On consulte la liste 'cats' à l'indice c[i], 
        # où la valeur 1 signifie que le chat est présent, et 0 qu'il est absent.
        if cats[c[i]] == 1:
            # Ce chat est déjà à l'intérieur, donc l'action est invalide.
            # On enregistre la position de cette action problématique.
            ans = i + 1
            # On arrête la vérification car on a trouvé une erreur.
            break
        else:
            # Le chat n'est pas encore à l'intérieur, on le marque comme présent.
            cats[c[i]] = 1
            # On ajoute ce chat au sommet de la pile pour garder la trace de son entrée.
            stack.append(c[i])
    else:
        # Ici, l'action est un entier négatif, ce qui signifie qu'un chat sort.
        # On considère l'identifiant absolu du chat qui sort avec '-c[i]'.

        # Vérifions si le chat qui devrait sortir est effectivement à l'intérieur.
        if cats[-c[i]] == 0:
            # Si le chat n'est pas à l'intérieur mais tente de sortir, l'action est invalide.
            # On enregistre la position de l'erreur.
            ans = i + 1
            # On arrête la vérification.
            break
        else:
            # Le chat est effectivement à l'intérieur, on le marque comme sorti.
            cats[-c[i]] = 0
            # On retire le chat au sommet de la pile, qui devrait correspondre à celui qui sort.
            # La pile suit donc la logique du dernier entré, premier sorti (LIFO).
            if(stack.pop() != -c[i]):
                # Si le chat qui sort n'est pas celui attendu en haut de la pile,
                # cela signifie que l'ordre de sortie est incorrect.
                # On enregistre la position de cette erreur.
                ans = i + 1
                # On arrête la vérification.
                break

# Après avoir traité toutes les actions, on vérifie si une erreur a été détectée.
if ans < 0:
    # Si 'ans' est toujours négatif, cela signifie que toutes les actions sont valides.
    print("OK")
else:
    # Sinon, on affiche le numéro (1-based index) de la première action invalide rencontrée.
    print(ans)