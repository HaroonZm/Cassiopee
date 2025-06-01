a, b = map(int, input().split())  # je prends deux entiers en entrée

# Conversion de a*b en une autre unité (je suppose), puis affichage avec 6 décimales
result = a * b / 3.305785
print("%.6f" % result)  # ouais, j'aime bien ce style ancien, mais ça marche quand même !