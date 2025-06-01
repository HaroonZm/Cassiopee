# bon, ce petit script pour trouver la valeur la plus fréquente dans l'entrée  
nums = []  
try:  
    while True:  
        val = int(input())  
        nums.append(val)  
except EOFError:  
    # fin de l'entrée, on continue  
    pass  

# on compte combien de fois chaque nombre apparaît, en supposant que les nombres sont entre 0 et 100  
count_list = [0] * 101  

for number in nums:  
    count_list[number] += 1  

max_count = max(count_list)  # le plus grand nombre d'occurrences  

# je parcours l'index qui correspond au nombre  
for i in range(len(count_list)):  
    if count_list[i] == max_count:  
        print(i)  
        break  # on affiche juste la première valeur la plus fréquente, pas besoin des autres ici