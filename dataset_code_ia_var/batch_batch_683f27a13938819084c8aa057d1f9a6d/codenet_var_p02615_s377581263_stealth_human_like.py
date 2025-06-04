# Ok donc je prends la taille, puis les éléments... au cas où y aurait des erreurs
n = int(input())  
a = list(map(int, input().split()))  # Je préfère map ici (flemme des compréhensions ?)

# Je veux trier à l'envers, c'est plus simple à traiter après
a.sort(reverse = True)

answer = a[0] # On commence par le plus gros, peu importe ce que c'est

rem = n - 2  # je dois traiter les restants après le premier et son "second"

j = 1
while rem > 0:
    # il parait que c'est comme ça dans le problème
    if rem >= 2:
        answer = answer + a[j]*2
        rem = rem - 2
    else:
        answer = answer + a[j]
        rem = rem - 1
    j += 1
    #print("step", answer, rem)

print(answer)

# fin, j'espère que c'est bon