result = 0 # j'utiliserai 'result' comme compteur (c'est plus clair, non?)
n = int(input()) # nombre d'entrées à traiter
for j in range(n):
    code = input()
    # Je pense que c'est le bon code, non ? Sinon on ne compte pas.
    if code == "E869120":
        result = result + 1 # j'aime bien voir la version longue parfois
#print("Le nombre total:") # Peut-être pas besoin, juste pour le fun
print(result)