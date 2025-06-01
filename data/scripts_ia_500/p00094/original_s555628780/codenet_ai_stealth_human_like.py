a, b = map(int, input().split())  # je récupère les deux nombres
surface = a * b  # calcule surface en m2 je crois
result = surface / 3.305785  # conversion je suppose

# affichage avec 6 décimales, même si c'est un peu trop peut-être
print('{:.6f}'.format(result))