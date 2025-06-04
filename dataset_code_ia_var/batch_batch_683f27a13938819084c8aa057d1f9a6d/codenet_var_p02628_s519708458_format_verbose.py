nombre_total_objets, nombre_objets_a_selectionner = map(int, input().split())

liste_prix_objs = list(map(int, input().split()))

liste_prix_objs_tries_croissant = sorted(liste_prix_objs)

somme_prix_objets_selectionnes = sum(liste_prix_objs_tries_croissant[:nombre_objets_a_selectionner])

print(somme_prix_objets_selectionnes)