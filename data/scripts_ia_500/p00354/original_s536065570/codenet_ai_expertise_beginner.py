jours = ["thu", "fri", "sat", "sun", "mon", "tue", "wed"]
numero = input("Entrez un nombre: ")
indice = int(numero) % 7
print(jours[indice])