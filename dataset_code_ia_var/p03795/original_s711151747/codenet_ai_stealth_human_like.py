# Bon, ici on va faire un ptit calcul...  
n = int(input())  # nombre de trucs à traiter ?

# Prix total avant réduc
total = n * 800 

# Réduc pour chaque 15, je crois que c'est ça
discounts = n // 15 * 200

total_price = total - discounts # Ouais ça marche

print(total_price)  # on affiche, voilà